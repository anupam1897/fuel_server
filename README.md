# Fuel Flask Server

##Overview
This Flask server serves as the backend infrastructure for the "Fuel" Flutter app, providing a reliable and efficient platform for managing fuel-related data. The server is designed to seamlessly handle data retrieval ensuring a smooth experience for users of the "Fuel" app.
Get to flutter fuel app at https://github.com/anupam1897/fuel

## Live Server

Host: AWS EC2 (Amazon Linux) \
 Database: RDS-mysql \
 Storage: AWS S3

## Base URL

base_url: http://54.165.87.139:8080/api/v1 \

For now all routes are public.

## Routes Table

| Endpoint        | Method | Description                             | Parameters | Example Request                                                   | Example Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------ | --------------------------------------- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/`             | GET    | Server Test                             | None       | `curl --location 'http://54.165.87.139:8080/'`                    | `server up and running`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `/get_posts`    | GET    | Retrieve all posts                      | None       | `curl --location 'http://54.165.87.139:8080/api/v1/get_posts'`    | `[{"caption":"Exploring beautiful landscapes!","createdAt":"Wed, 24 Jan 2024 17:35:46 GMT","likes":"99862","postImage":null,"post_id":2,"profilePicture":"https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/avatars/24998e20-06ec-43bc-b81a-d01a3864938e.jpg","username":"user123","views":"3126174"}, // Additional entries... ]`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `/get_ventures` | GET    | Retrieve all information about ventures | None       | `curl --location 'http://54.165.87.139:8080/api/v1/get_ventures'` | `[{"description":"Apple Inc. is a multinational technology company renowned for its innovative consumer electronics, software, and services. Widely recognized for iconic products like the iPhone, iPad, and Mac, Apple has consistently set industry standards in design, user experience, and technological advancements","employeeCount":7548,"founder_name":"Steve Jobs","fundingRounds":"None","fundingStatus":"Well Funded","incorporationDate":null,"incorporationType":"Incoporated","industryCategory":"fintech","investor":"Sequoia","location":"Cupertino, LA","logo_icon_src":"https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/company-logos/00d9360a-761f-47a4-9296-0650286da5dd.png","rating":"4","type":"technology","valuation":2147483647,"venture_id":1,"venture_name":"Apple"}, // Additional entries... ] }` |
| `/get_ads`      | GET    | Retrieve all image src for ads          | None       | `curl --location 'http://54.165.87.139:8080/api/v1/get_ads'`      | `[{"ad_id":1,"ad_image":"https://fuel-bucket-001.s3.ap-south-1.amazonaws.com/ads/00a7ec6c-4309-4db9-a2f1-5d365c013e72.jpg"}, // Additional entries... ] }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Upcoming Features:

- Remaining routes for create and update
- Webtoken for user authentication and authorization enhancing security
- Rate Limiting for api routes based on IP

## Getting Started

You can use above routes for this or Install on your own local machine

Prerequisites
Python 3.11
Flask

### Installation

Clone the repository: `git clone https://github.com/anupam1897/fuel_server.git`

Navigate to the project directory:
`cd fuel-flask-server`

Install dependencies:
`pip install -r requirements.txt `

### Configuration

Configure the server settings in config.py to match your environment.

## Running the Server

Execute the following command to start the Flask server: \
`python app.py` \
The server will be running at http://localhost:8080 by default.

### API Documentation:

Authentication mechanisms: None

Deployment
The Flask server is deployed on an AWS EC2 instance for optimal scalability and availability. [Provide additional deployment instructions if needed.]

## Acknowledgments

I would like to express my gratitude to the following open-source projects and their contributors, whose work has significantly contributed to the development of my Flutter application:

- [flutter_svg](https://pub.dev/packages/flutter_svg) v2.0.9

  - Thank you to the developers for providing a versatile SVG rendering library for Flutter, enhancing my app's visual elements.

- [intl](https://pub.dev/packages/intl) v0.19.0

  - Special thanks to the intl package contributors for their efforts in making internationalization and localization seamless in Flutter.

- [video_player](https://pub.dev/packages/video_player) v2.8.2

  - I appreciate the video_player team for creating a robust video playback solution, improving the multimedia experience in my app.

- [provider](https://pub.dev/packages/provider) v6.1.1

  - Kudos to the provider package maintainers for offering a powerful state management solution that simplifies my app's architecture.

- [google_fonts](https://pub.dev/packages/google_fonts) v4.0.4

  - Thanks to the google_fonts developers for providing an easy-to-use package that enhances my app's typography.

- [connectivity](https://pub.dev/packages/connectivity) v3.0.6

  - A big shoutout to the connectivity package maintainers for their work in enabling my app to monitor network connectivity seamlessly.

- [lottie](https://pub.dev/packages/lottie) v1.0.1
  - My appreciation goes to the lottie package contributors for integrating Lottie animations into Flutter, adding a dynamic visual element to this app.

I extend my heartfelt thanks to all the open-source contributors who dedicate their time and effort to building these fantastic packages, making the Flutter development community thrive.

## For Recruiters

Thank you for considering Fuel for review! I believe that Fuel showcases my commitment to creating user-friendly and feature-rich Flutter applications. If you have any questions or need further information, please feel free to reach out to me. I'm excited about the opportunity to discuss coding practices, design decisions, and the overall development process behind Fuel.

This app is fairly very new and I'm passionate about continuous improvement, and ready to contribute to making Fuel even better. I believe in collaborating with a dynamic team and leveraging our skills to serve a broader audience and enhance the user experience. I would be excited to hear from you about possibilities of collaboration.

I appreciate your time and look forward to the possibility of working together.

Contact: Anupam Chauhan \
 anupam1897@gmail.com
