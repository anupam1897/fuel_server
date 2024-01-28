from flask import Flask, jsonify
import json, os,  uuid, boto3
from mysql.connector import connect
# AWS S3 Client
s3 = boto3.client(
    's3', 
    aws_access_key_id    = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name          = os.environ.get("AWS_REGION"),
	)

# Mysql connection
conn = connect(
	host =os.environ.get("RDS_MYSQL_HOST"),
	port =os.environ.get("RDS_MYSQL_PORT"),
	user =os.environ.get("RDS_MYSQL_USER"),
	password =os.environ.get("RDS_MYSQL_PASSWORD"),
	database = os.environ.get("RDS_MYSQL_DATABASE"),
	) 

def generate_uuid_filename(original_filename):
    """
    Generate a UUID and append it to the original filename.
    
    Parameters:
    - original_filename: The original filename with its extension.

    Returns:
    - A new filename with a UUID and the original file extension.
    """
    # Extract file extension
    _, file_extension = os.path.splitext(original_filename)

    # Generate UUID
    uuid_string = str(uuid.uuid4())

    # Concatenate UUID and file extension
    new_filename = uuid_string + file_extension

    return new_filename


# -----------------------POSTS UPLOAD------------------------------
bucket_name = 'fuel-bucket-001'
content_type = 'image/jpeg'
lst = [file for file in os.listdir("./posts")]
key_list = []
try:
    for name in lst:
        key =  "posts/" + generate_uuid_filename(name)
        s3.upload_file('./posts/' + name, bucket_name, key, ExtraArgs={'ContentType': content_type})

except Exception as e:
    raise e


# -----------------------PROFILE PICTURE UPLOAD------------------------------

lst = [file for file in os.listdir("./ads")]
try:
    for name in lst:
        key =  "ads/" + generate_uuid_filename(name)
        s3.upload_file('./ads/' + name, bucket_name, key, ExtraArgs={'ContentType': content_type})

except Exception as e:
    raise e


# -----------------------PROFILE PICTURE UPLOAD------------------------------

lst = [file for file in os.listdir("./avatars")]
try:
    for name in lst:
        key =  "avatars/" + generate_uuid_filename(name)
        s3.upload_file('./avatars/' + name, bucket_name, key, ExtraArgs={'ContentType': content_type})

except Exception as e:
    raise e


# -----------------------PROFILE PICTURE UPLOAD------------------------------

lst = [file for file in os.listdir("./company logos")]
try:
    for name in lst:
        key =  "company-logos/" + generate_uuid_filename(name)
        s3.upload_file('./company logos/' + name, bucket_name, key, ExtraArgs={'ContentType': content_type})

except Exception as e:
    raise e

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# get all images-url

response = s3.list_objects_v2(Bucket='fuel-bucket-001', Prefix='avatars/')
# Extract all object keys
keys = [obj['Key'] for obj in response.get('Contents', [])]
url = 'https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/'
list_url = [url + key for key in keys]


# === === === === === === === ===

cursor = conn.cursor()
i = 1
for url in list_url[2:48]:
    x = '"'+url+ '"'
    query  = "UPDATE posts SET profilePicture = "+ x +" WHERE post_id = "+ str(i)  +";"
    print(query)
    cursor.execute(query)
    conn.commit()
    i = i + 1
conn.close()



cursor = conn.cursor()
i = 1
for url in list_url[2:48]:
    x = '"'+url+ '"'
    query  = "UPDATE posts SET profilePicture = "+ x +" WHERE post_id = "+ str(i)  +";"
    print(query)
    cursor.execute(query)
    conn.commit()
    i = i + 1
conn.close()

cursor = conn.cursor()
i = 1
for url in list_url:
    x = '"'+url+ '"'
    query  = "UPDATE posts SET postImage = "+ x +" WHERE post_id = "+ str(i)  +";"
    print(query)
    cursor.execute(query)
    conn.commit()
    i = i + 2
conn.close()


lst = [

  {
    "profilePicture": "https:s3/bucket=users/profile/90325124.jpg",
    "username": "user123",
    "postImage": "https:s3/bucket=posts/324dvnjdj355qgrijdnv.jpg",
    "caption": "Exploring beautiful landscapes!",
    "views": 3126174,
    "likes": 99862
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "traveler22",
    "caption": "City lights at night!",
    "views": 2831983,
    "likes": 83229
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "foodie_gal",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Delicious homemade pizza!",
    "views": 9996440,
    "likes": 17926
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "fitness_freak",
    "caption": "Morning run vibes!",
    "views": 6164727,
    "likes": 27205
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "artsy_soul",
    "postImage": "https:s3/bucket=posts/2233445566.jpg",
    "caption": "Capturing the beauty of nature!",
    "views": 8082141,
    "likes": 17809
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/34567890.jpg",
    "username": "gamer_x",
    "caption": "Gaming night with friends!",
    "views": 3464702,
    "likes": 80282
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/23456789.jpg",
    "username": "music_lover",
    "postImage": "https:s3/bucket=posts/3344556677.jpg",
    "caption": "Lost in the melody!",
    "views": 2150060,
    "likes": 20867
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "fashionista",
    "caption": "OOTD - Stylish and comfy!",
    "views": 2891751,
    "likes": 85977
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "tech_enthusiast",
    "postImage": "https:s3/bucket=posts/4455667788.jpg",
    "caption": "Geeking out with the latest tech!",
    "views": 2582617,
    "likes": 78830
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "petlover",
    "caption": "Quality time with my furry friend!",
    "views": 6891475,
    "likes": 13026
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/45678901.jpg",
    "username": "explorer2025",
    "postImage": "https:s3/bucket=posts/5566778899.jpg",
    "caption": "Sunset at the beach!",
    "views": 3037374,
    "likes": 92414
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "bookworm23",
    "caption": "Diving into a good book!",
    "views": 3342008,
    "likes": 43131
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "fitness_junkie",
    "postImage": "https:s3/bucket=posts/6677889900.jpg",
    "caption": "Powerful workout session!",
    "views": 1386802,
    "likes": 15214
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "cooking_magic",
    "caption": "Creating culinary masterpieces!",
    "views": 9301888,
    "likes": 32429
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "coding_geek",
    "postImage": "https:s3/bucket=posts/7788990011.jpg",
    "caption": "Late-night coding vibes!",
    "views": 2908531,
    "likes": 51141
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/34567890.jpg",
    "username": "yoga_love",
    "caption": "Finding inner peace through yoga!",
    "views": 3826616,
    "likes": 64276
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/23456789.jpg",
    "username": "gaming_guru",
    "postImage": "https:s3/bucket=posts/8899001122.jpg",
    "caption": "Epic gaming moments!",
    "views": 4423832,
    "likes": 27230
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "fashion_forward",
    "caption": "Rocking the latest fashion trends!",
    "views": 3558875,
    "likes": 51054
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "tech_enthusiast2",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Exciting tech discoveries!",
    "views": 9970704,
    "likes": 30679
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "pet_parent",
    "caption": "Adventures with my furry companions!",
    "views": 9947968,
    "likes": 96684
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/45678901.jpg",
    "username": "nature_admirer",
    "postImage": "https:s3/bucket=posts/5566778899.jpg",
    "caption": "Embracing the beauty of the wilderness!",
    "views": 3275010,
    "likes": 27869
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "food_explorer",
    "caption": "Culinary adventures around the world!",
    "views": 82478,
    "likes": 7899
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "health_wellness",
    "postImage": "https:s3/bucket=posts/6677889900.jpg",
    "caption": "Promoting a healthy lifestyle!",
    "views": 5549947,
    "likes": 61439
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "entrepreneur_life",
    "caption": "Building dreams, one venture at a time!",
    "views": 8813507,
    "likes": 7283
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "artsy_soul2",
    "postImage": "https:s3/bucket=posts/7788990011.jpg",
    "caption": "Expressing creativity through art!",
    "views": 1248492,
    "likes": 12662
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/34567890.jpg",
    "username": "motorsport_lover",
    "caption": "Adrenaline-fueled race day!",
    "views": 2343805,
    "likes": 73442
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/23456789.jpg",
    "username": "podcast_enthusiast",
    "postImage": "https:s3/bucket=posts/8899001122.jpg",
    "caption": "Diving into interesting conversations!",
    "views": 1583055,
    "likes": 63319
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "gardening_passion",
    "caption": "Nurturing plants and growing joy!",
    "views": 4182375,
    "likes": 69257
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "film_buff",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Movie night essentials!",
    "views": 5649791,
    "likes": 81138
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "mountain_explorer",
    "caption": "Scaling new heights!",
    "views": 8995133,
    "likes": 90620
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "architecture_aficionado",
    "postImage": "https:s3/bucket=posts/6677889900.jpg",
    "caption": "Marveling at architectural wonders!",
    "views": 3441729,
    "likes": 67823
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "cycling_enthusiast",
    "caption": "Pedaling through scenic routes!",
    "views": 1164274,
    "likes": 8768
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "coffeelover",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Savoring the perfect brew!",
    "views": 6357418,
    "likes": 3026
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "coding_enthusiast3",
    "caption": "Code, debug, repeat!",
    "views": 2880613,
    "likes": 58646
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "adventure_seeker",
    "postImage": "https:s3/bucket=posts/6677889900.jpg",
    "caption": "Thriving on adrenaline!",
    "views": 1819474,
    "likes": 64721
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "coding_enthusiast4",
    "postImage": "https:s3/bucket=posts/7788990011.jpg",
    "caption": "Solving complex problems with code!",
    "views": 6524832,
    "likes": 71030
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/34567890.jpg",
    "username": "beach_lover",
    "caption": "Chasing waves and sandy toes!",
    "views": 8405992,
    "likes": 16208
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/23456789.jpg",
    "username": "music_enthusiast2",
    "postImage": "https:s3/bucket=posts/8899001122.jpg",
    "caption": "Eclectic playlist for the soul!",
    "views": 191633,
    "likes": 59545
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "gym_motivation",
    "caption": "Pushing limits at the gym!",
    "views": 1488810,
    "likes": 22232
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "pet_photographer",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Capturing adorable moments of pets!",
    "views": 3483985,
    "likes": 41926
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "booklover2",
    "postImage": "https:s3/bucket=posts/7788990011.jpg",
    "caption": "Dive into a good book!",
    "views": 7699670,
    "likes": 18382
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/90123456.jpg",
    "username": "snow_adventures",
    "caption": "Embracing the winter wonderland!",
    "views": 3044569,
    "likes": 65446
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/78901234.jpg",
    "username": "fashionista2",
    "postImage": "https:s3/bucket=posts/1122334455.jpg",
    "caption": "Styled for the runway!",
    "views": 2033739,
    "likes": 95870
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/56789012.jpg",
    "username": "gamer_life",
    "caption": "Leveling up in the gaming world!",
    "views": 5615529,
    "likes": 10236
  },
  {
    "profilePicture": "https:s3/bucket=users/profile/12345678.jpg",
    "username": "hiking_adventures",
    "postImage": "https:s3/bucket=posts/7788990011.jpg",
    "caption": "Trails and scenic views!",
    "views": 8943603,
    "likes": 27623
  }
]

cursor = conn.cursor()
for body in lst:
    username = '"' + body["username"] + '"'
    caption = '"'+body["caption"]+'"'
    views  = body["views"]
    likes  = body["likes"]
    query  = "INSERT INTO posts(username,caption,views,likes) VALUES( "+str(username)+ "," +caption+","+ str(views)+ "," +str(likes)+ ");"
    print(query)
    cursor.execute(query)
    conn.commit()
conn.close()



