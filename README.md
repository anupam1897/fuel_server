###Fuel Flask Server

##Overview
This Flask server serves as the backend infrastructure for the "Fuel" Flutter app, providing a reliable and efficient platform for managing fuel-related data. The server is designed to seamlessly handle data retrieval ensuring a smooth experience for users of the "Fuel" app.

# Live Server
Host: AWS EC2 (Amazon Linux)
DB: RDS-mysql
Storage: AWS S3

# Base URL
For now all routes are public. 
# Routes Table

| Endpoint                 | Method | Description                        | Parameters                          | Example Request                                       | Example Response                                    |
|--------------------------|--------|------------------------------------|-------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| `/fuel_entries`          | GET    | Retrieve fuel entries              | `start_date` (optional)<br>`end_date` (optional) | `curl -X GET https://api.fuelapp.com/v1/fuel_entries?start_date=2023-01-01&end_date=2023-12-31` | `{ "fuel_entries": [ { "id": 1, "date": "2023-05-15", "fuel_type": "Gasoline", "price": 3.50, "mileage": 300, "location": "Gas Station A" }, // Additional entries... ] }` |
| `/fuel_entries`          | POST   | Add a new fuel entry               | `date` (required)<br>`fuel_type` (required)<br>`price` (required)<br>`mileage` (required)<br>`location` (optional) | `curl -X POST -H "Content-Type: application/json" -d '{"date": "2023-06-10", "fuel_type": "Gasoline", "price": 3.60, "mileage": 320, "location": "Gas Station B"}' https://api.fuelapp.com/v1/fuel_entries` | `{ "id": 2, "date": "2023-06-10", "fuel_type": "Gasoline", "price": 3.60, "mileage": 320, "location": "Gas Station B" }` |
| `/fuel_entries`          | POST   | Add a new fuel entry               | `date` (required)<br>`fuel_type` (required)<br>`price` (required)<br>`mileage` (required)<br>`location` (optional) | `curl -X POST -H "Content-Type: application/json" -d '{"date": "2023-06-10", "fuel_type": "Gasoline", "price": 3.60, "mileage": 320, "location": "Gas Station B"}' https://api.fuelapp.com/v1/fuel_entries` | `{ "id": 2, "date": "2023-06-10", "fuel_type": "Gasoline", "price": 3.60, "mileage": 320, "location": "Gas Station B" }` |



# Upcoming Features:
- Webtoken for user authentication and authorization enhancing security
- Rate Limiting for api routes based on IP


Getting Started
Prerequisites
Python 3.x
Flask
[Additional dependencies, if any]
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/fuel-flask-server.git
Navigate to the project directory:

bash
Copy code
cd fuel-flask-server
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configuration
Configure the server settings in config.py to match your environment.
Running the Server
Execute the following command to start the Flask server:

bash
Copy code
python app.py
The server will be running at http://localhost:5000 by default.

API Documentation
[Document the available API endpoints, request/response formats, and authentication mechanisms, if any.]

Deployment
The Flask server is deployed on an AWS EC2 instance for optimal scalability and availability. [Provide additional deployment instructions if needed.]

Contributors
[Your Name]
[Other contributors, if any]
License
This project is licensed under the [License Name] - see the LICENSE.md file for details.

Acknowledgments
[Optional: Acknowledge any third-party libraries, services, or resources that were used in the development of the Flask server.]

Feel free to customize this README template according to your specific project details and requirements.
