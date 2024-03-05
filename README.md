A brief description of what this project does and who it's for

Project Description This project entails the development of a robust Flask server in Python, equipped with various powerful capabilities:

REST API Endpoints: Crawl Handler:

Located in the crawl_controller.py file, this handler serves as the gateway for crawling new web pages. Endpoint: POST /crawl Functionality: Accepts JSON payloads containing a URL and a notification preference. Initiates crawling processes for the provided URL. Upon successful initiation: Creates a new crawl instance in the database with a status of "Accepted". Returns the unique ID of the crawl to the client. Concurrently fetches the HTML content of the URL, saving it locally to a file. Updates the file path in the database upon completion. Updates the status to "Complete". Status Query Handler:

The second API endpoint is designed to retrieve the status of existing crawls. Endpoint: GET /crawl/status/<crawl_id> Functionality: Accepts a crawl ID as a parameter. Queries the database to retrieve the status of the specified crawl. Returns the status (ACCEPTED/COMPLETED/ERROR/NOT_FOUND) to the client. If the crawl ID is not found, it returns a "Crawl ID not found" message. Usage: Crawl Handler: To initiate crawling, send a POST request to http://127.0.0.1:5000/crawl with the following JSON payload:

json Copy code { "url": "example.com", "notification_preference": "email" } Performance: The server returns the new crawl_id to the user immediately and performs the remaining tasks in the background, ensuring faster processing for multiple users.

Points to Improve: Implement uploading HTML content to Amazon S3 using boto3 for enhanced resource management. Testing: Simple tests have been written as part of the implementation: crawl_test.py crawl_facade_test.py Prerequisites to Run the Server: Ensure Python 3 is installed. Postgres should be installed on the machine with the database created. Initialize environment variables with the connection string: "postgresql://postgres:password@localhost:5432/" Install dependencies listed in requirements.txt using pip: pip install -r requirements.txt
