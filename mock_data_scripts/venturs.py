import random, os
from mysql.connector import connect
import boto3
# AWS S3 Client
s3 = boto3.client(
    's3', 
    aws_access_key_id    = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name          = os.environ.get("AWS_REGION"),
	)

conn = connect(
	host =os.environ.get("RDS_MYSQL_HOST"),
	port =os.environ.get("RDS_MYSQL_PORT"),
	user =os.environ.get("RDS_MYSQL_USER"),
	password =os.environ.get("RDS_MYSQL_PASSWORD"),
	database = os.environ.get("RDS_MYSQL_DATABASE"),
	) 

lst = [
  {
    "venture_name": "Apple",
    "founders": "Steve Jobs",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/apple.png",
    "rating": 4.4,
    "valuation": 10233210220,
    "location": "Cupertino, LA",
    "incorporationDate": "12-12-2004",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "fintech",
    "fundingRounds": "None",
    "investors": "Sequoia",
    "fundingStatus": "Well Funded",
    "employeeCount": 7548,
    "description": "Apple Inc. is a multinational technology company renowned for its innovative consumer electronics, software, and services. Widely recognized for iconic products like the iPhone, iPad, and Mac, Apple has consistently set industry standards in design, user experience, and technological advancements"
  },
  {
    "venture_name": "Microsoft",
    "founders": "Bill Gates",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/microsoft.png",
    "rating": 4.6,
    "valuation": 55268769607,
    "location": "Redmond, WA",
    "incorporationDate": "04-04-1975",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "software",
    "fundingRounds": "None",
    "investors": "Vulcan Capital",
    "fundingStatus": "Well Funded",
    "employeeCount": 94138,
    "description": "Microsoft is a global technology company known for its software products, including the Windows operating system and Office suite, as well as cloud services like Azure."
  },
  {
    "venture_name": "Amazon",
    "founders": "Jeff Bezos",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/amazon.png",
    "rating": 4.7,
    "valuation": 12892677149,
    "location": "Seattle, WA",
    "incorporationDate": "07-05-1994",
    "incorporationType": "Incoporated",
    "type": "e-commerce",
    "industryCategory": "retail",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 24060,
    "description": "Amazon is a multinational technology and e-commerce company known for its vast online retail platform, cloud computing services (AWS), and digital streaming services."
  },
  {
    "venture_name": "Google",
    "founders": "Larry Page",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/google.png",
    "rating": 4.8,
    "valuation": 3253895124,
    "location": "Mountain View, CA",
    "incorporationDate": "09-04-1998",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "search engine",
    "fundingRounds": "None",
    "investors": "Alphabet Inc.",
    "fundingStatus": "Well Funded",
    "employeeCount": 88142,
    "description": "Google is a global technology company specializing in internet-related services and products, including search engines, online advertising, and cloud computing."
  },
  {
    "venture_name": "Tesla",
    "founders": "Elon Musk",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/tesla.png",
    "rating": 4.5,
    "valuation": 57343698843,
    "location": "Palo Alto, CA",
    "incorporationDate": "07-01-2003",
    "incorporationType": "Incoporated",
    "type": "automotive",
    "industryCategory": "electric vehicles",
    "fundingRounds": "None",
    "investors": "Baillie Gifford",
    "fundingStatus": "Well Funded",
    "employeeCount": 69028,
    "description": "Tesla is a leading electric vehicle and clean energy company, known for its innovative approach to sustainable transportation and energy solutions."
  },
  {
    "venture_name": "Facebook",
    "founders": "Mark Zuckerberg",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/facebook.png",
    "rating": 4.2,
    "valuation": 68418143718,
    "location": "Menlo Park, CA",
    "incorporationDate": "02-04-2004",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "social media",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 18537,
    "description": "Facebook is a social media giant connecting people worldwide, offering a platform for sharing content, connecting with friends, and advertising."
  },
  {
    "venture_name": "Netflix",
    "founders": "Reed Hastings",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/netflix.png",
    "rating": 4.1,
    "valuation": 5543424683,
    "location": "Los Gatos, CA",
    "incorporationDate": "08-29-1997",
    "incorporationType": "Incoporated",
    "type": "entertainment",
    "industryCategory": "streaming",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 71788,
    "description": "Netflix is a global streaming service providing a wide variety of TV shows, movies, documentaries, and original content on demand."
  },
  {
    "venture_name": "SpaceX",
    "founders": "Elon Musk",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/spacex.png",
    "rating": 4.9,
    "valuation": 53564801465,
    "location": "Hawthorne, CA",
    "incorporationDate": "03-14-2002",
    "incorporationType": "Incoporated",
    "type": "aerospace",
    "industryCategory": "space exploration",
    "fundingRounds": "None",
    "investors": "Baillie Gifford",
    "fundingStatus": "Well Funded",
    "employeeCount": 40809,
    "description": "SpaceX is a private aerospace manufacturer and space transportation company known for its ambitious goals in space exploration and colonization."
  },
  {
    "venture_name": "Uber",
    "founders": "Travis Kalanick",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/uber.png",
    "rating": 4.3,
    "valuation": 63206857909,
    "location": "San Francisco, CA",
    "incorporationDate": "03-14-2009",
    "incorporationType": "Incoporated",
    "type": "transportation",
    "industryCategory": "ridesharing",
    "fundingRounds": "None",
    "investors": "SoftBank",
    "fundingStatus": "Well Funded",
    "employeeCount": 9816,
    "description": "Uber is a global ridesharing and food delivery platform, connecting users with transportation and delivery services through its mobile app."
  },
  {
    "venture_name": "Airbnb",
    "founders": "Brian Chesky",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/airbnb.png",
    "rating": 4.5,
    "valuation": 74680001593,
    "location": "San Francisco, CA",
    "incorporationDate": "08-05-2008",
    "incorporationType": "Incoporated",
    "type": "hospitality",
    "industryCategory": "short-term rentals",
    "fundingRounds": "None",
    "investors": "Sequoia",
    "fundingStatus": "Well Funded",
    "employeeCount": 71701,
    "description": "Airbnb is a global online marketplace that enables people to list, discover, and book unique accommodations and experiences around the world."
  },
  {
    "venture_name": "Twitter",
    "founders": "Jack Dorsey",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/twitter.png",
    "rating": 4.0,
    "valuation": 14628546461,
    "location": "San Francisco, CA",
    "incorporationDate": "03-21-2006",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "social media",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 1463,
    "description": "Twitter is a widely-used social media platform where users can post and interact with short messages, known as tweets, sharing thoughts and news in real-time."
  },
  {
    "venture_name": "Airbus",
    "founders": "Roger B teille",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/airbus.png",
    "rating": 4.2,
    "valuation": 49686907378,
    "location": "Leiden, Netherlands",
    "incorporationDate": "05-29-1969",
    "incorporationType": "Incoporated",
    "type": "aerospace",
    "industryCategory": "commercial aircraft",
    "fundingRounds": "None",
    "investors": "European Investment Bank",
    "fundingStatus": "Well Funded",
    "employeeCount": 97275,
    "description": "Airbus is a European multinational aerospace corporation known for manufacturing commercial aircraft, military aircraft, and satellites."
  },
  {
    "venture_name": "Johnson & Johnson",
    "founders": "Robert Wood Johnson I",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/jnj.png",
    "rating": 4.6,
    "valuation": 7169036255,
    "location": "New Brunswick, NJ",
    "incorporationDate": "01-01-1886",
    "incorporationType": "Incoporated",
    "type": "healthcare",
    "industryCategory": "pharmaceuticals",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 88903,
    "description": "Johnson & Johnson is a global healthcare company focused on pharmaceuticals, medical devices, and consumer goods."
  },
  {
    "venture_name": "Alibaba Group",
    "founders": "Jack Ma",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/alibaba.png",
    "rating": 4.7,
    "valuation": 46975292484,
    "location": "Hangzhou, China",
    "incorporationDate": "04-04-1999",
    "incorporationType": "Incoporated",
    "type": "e-commerce",
    "industryCategory": "online retail",
    "fundingRounds": "None",
    "investors": "SoftBank",
    "fundingStatus": "Well Funded",
    "employeeCount": 5439,
    "description": "Alibaba Group is a Chinese multinational conglomerate specializing in e-commerce, retail, internet, and technology."
  },
  {
    "venture_name": "Pfizer",
    "founders": "Charles Pfizer",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/pfizer.png",
    "rating": 4.5,
    "valuation": 9634725597,
    "location": "New York, NY",
    "incorporationDate": "08-06-1849",
    "incorporationType": "Incoporated",
    "type": "healthcare",
    "industryCategory": "pharmaceuticals",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 96289,
    "description": "Pfizer is a leading pharmaceutical company engaged in the research, development, and manufacturing of healthcare products."
  },
  {
    "venture_name": "IBM",
    "founders": "Charles Ranlett Flint",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/ibm.png",
    "rating": 4.2,
    "valuation": 33550191140,
    "location": "Armonk, NY",
    "incorporationDate": "06-16-1911",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "information technology",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 40289,
    "description": "IBM (International Business Machines Corporation) is a multinational technology company providing hardware, software, and services."
  },
  {
    "venture_name": "Nestle",
    "founders": "Henry Nestle",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/nestle.png",
    "rating": 4.5,
    "valuation": 87349164886,
    "location": "Vevey, Switzerland",
    "incorporationDate": "08-03-1866",
    "incorporationType": "Incoporated",
    "type": "food and beverage",
    "industryCategory": "consumer goods",
    "fundingRounds": "None",
    "investors": "BlackRock",
    "fundingStatus": "Well Funded",
    "employeeCount": 52955,
    "description": "Nestle is a Swiss multinational food and drink processing conglomerate, known for its wide range of consumer goods."
  },
  {
    "venture_name": "Cisco",
    "founders": "Leonard Bosack",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/cisco.png",
    "rating": 4.3,
    "valuation": 9563992847,
    "location": "San Jose, CA",
    "incorporationDate": "12-10-1984",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "networking hardware",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 89454,
    "description": "Cisco is a global technology company specializing in networking hardware, software, and telecommunications equipment."
  },
  {
    "venture_name": "Procter & Gamble",
    "founders": "William Procter",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/pg.png",
    "rating": 4.4,
    "valuation": 33424787568,
    "location": "Cincinnati, OH",
    "incorporationDate": "10-31-1837",
    "incorporationType": "Incoporated",
    "type": "consumer goods",
    "industryCategory": "household and personal care",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 35476,
    "description": "P&G is a leader in the consumer goods industry, offering globally recognized brands across categories such as beauty, health, hygiene, and cleaning."
  },
  {
    "venture_name": "Sony",
    "founders": "Masaru Ibuka",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/sony.png",
    "rating": 4.5,
    "valuation": 26971658830,
    "location": "Tokyo, Japan",
    "incorporationDate": "05-07-1946",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "electronics",
    "fundingRounds": "None",
    "investors": "BlackRock",
    "fundingStatus": "Well Funded",
    "employeeCount": 39010,
    "description": "Sony is a Japanese multinational conglomerate known for its diverse range of electronics, gaming, entertainment, and financial services."
  },
  {
    "venture_name": "General Electric (GE)",
    "founders": "Thomas Edison",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/ge.png",
    "rating": 4.1,
    "valuation": 12908902538,
    "location": "Boston, MA",
    "incorporationDate": "04-15-1892",
    "incorporationType": "Incoporated",
    "type": "conglomerate",
    "industryCategory": "industrial",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 63182,
    "description": "General Electric (GE) is a multinational conglomerate with operations in aviation, healthcare, power, renewable energy, and more."
  },
  {
    "venture_name": "Oracle Corporation",
    "founders": "Larry Ellison",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/oracle.png",
    "rating": 4.2,
    "valuation": 48947125906,
    "location": "Redwood City, CA",
    "incorporationDate": "06-16-1977",
    "incorporationType": "Incoporated",
    "type": "technology",
    "industryCategory": "software",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 62933,
    "description": "Oracle Corporation is a multinational computer technology corporation known for its database management systems and cloud solutions."
  },
  {
    "venture_name": "The Coca-Cola Company",
    "founders": "John Stith Pemberton",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/coca-cola.png",
    "rating": 4.3,
    "valuation": 66515847892,
    "location": "Atlanta, GA",
    "incorporationDate": "01-29-1892",
    "incorporationType": "Incoporated",
    "type": "beverages",
    "industryCategory": "soft drinks",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 41507,
    "description": "The Coca-Cola Company is a global beverage corporation, known for its iconic soft drink Coca-Cola and a wide range of other beverages."
  },
  {
    "venture_name": "Boeing",
    "founders": "William E. Boeing",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/boeing.png",
    "rating": 4.1,
    "valuation": 61777875561,
    "location": "Chicago, IL",
    "incorporationDate": "07-15-1916",
    "incorporationType": "Incoporated",
    "type": "aerospace",
    "industryCategory": "commercial airplanes",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 55728,
    "description": "Boeing is an aerospace company specializing in the design, manufacture, and support of commercial and military aircraft."
  },
  {
    "venture_name": "McDonald's Corporation",
    "founders": "Ray Kroc",
    "logo_icon_src": "https:s3/bucket=ventureInfo/logos/icon/mcdonalds.png",
    "rating": 4.0,
    "valuation": 6732953036,
    "location": "Chicago, IL",
    "incorporationDate": "04-15-1955",
    "incorporationType": "Incoporated",
    "type": "food",
    "industryCategory": "fast food",
    "fundingRounds": "None",
    "investors": "Vanguard Group",
    "fundingStatus": "Well Funded",
    "employeeCount": 23351,
    "description": " Headquartered in Chicago, Illinois, McDonald's is synonymous with the golden arches, serving millions of customers globally with its signature menu of burgers, fries, beverages, and more."
  }
]




# ---------------------CREATING VENTURE TABLE---------------------------
cursor = conn.cursor()
for i in lst:
    venture_name = '"'+i['venture_name']+'"'
    founders = '"'+i['founders']+'"'
    rating = '"'+str(i['rating'])+'"'
    valuation = '"'+str(i['valuation'])+'"'
    location = '"'+i['location']+'"'
    incorporationType = '"'+i['incorporationType']+'"'
    type = '"'+i['type']+'"'
    industryCategory = '"'+i['industryCategory']+'"'
    fundingRounds = '"'+i['fundingRounds']+'"'
    investors = '"'+i['investors']+'"'
    fundingStatus = '"'+i['fundingStatus']+'"'
    employeeCount = '"'+str(i['employeeCount'])+'"'
    desc = '"'+i['description']+'"'
    query  = "INSERT INTO ventures( venture_name , founder_name  , rating , valuation , location  , incorporationType , type , industryCategory , fundingRounds  , investor , fundingStatus , employeeCount  , description ) VALUES( " +venture_name + "," +founders+ "," +rating+ "," +valuation+ "," +location+ "," +incorporationType+ "," +type+ "," +industryCategory+ "," +fundingRounds+ "," +investors+ "," +fundingStatus+ "," +employeeCount+ "," +desc + ");"

    print(query)
    cursor.execute(query)
    conn.commit()
conn.close()





# ---------------------GETTING  LOGO ICON SRC---------------------------
response = s3.list_objects_v2(Bucket='fuel-bucket-001', Prefix='company-logos/')
# Extract all object keys
keys = [obj['Key'] for obj in response.get('Contents', [])]
url = 'https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/'
list_url = [url + key for key in keys]

# ---------------------UPDATING LOGO ICON SRC---------------------------
cursor = conn.cursor()
i = 1
for url in list_url[0:26]:
    x = '"'+url+ '"'
    query  = "UPDATE ventures SET logo_icon_src = "+ x +" WHERE venture_id = "+ str(i)  +";"
    print(query)
    cursor.execute(query)
    conn.commit()
    i = i + 1
conn.close()





