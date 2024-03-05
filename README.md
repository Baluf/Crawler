In this assignment, I've crafted a robust Flask server in Python, equipped with a range of powerful capabilities:
REST API Endpoints:
● Crawl Handler: This handler, located in the crawl_controller.py file, serves as the gateway for crawling new web pages.
● Endpoint: POST /crawl ● Functionality:
● Accepts JSON payloads containing a URL and a notification preference.
● Initiates crawling processes for the provided URL.
● Upon successful initiation:
● Creates a new crawl instance in the database with a status of "Accepted".
● Returns the unique ID of the crawl to the client.
● Concurrently fetches the HTML content of the URL, saving it
locally to file..
● Updates the file path in the database upon completion.
● Updates the status to "Complete".
● Status Query Handler: The second API endpoint is designed to retrieve the status of existing crawls.
● Endpoint: GET /crawl/status/<crawl_id> ● Functionality:
● Accepts a crawl ID as a parameter.
● Queries the database to retrieve the status of the specified crawl.
● Returns the status
(ACCEPTED/COMPLETED/ERROR/NOT_FOUND) to the client.
● If the crawl ID is not found, it returns a "Crawl ID not found" message.
Usage:
● Crawl Handler:
● To initiate crawling, send a POST request to http://127.0.0.1:5000/crawl with the following JSON payload:
Performance:
The server returns to the user immediately the new crawl_id and doing the left job in the background to do a faster job for multiple users.
Points to improve:
1. I would also upload to s3 the html content (using boto3) files but lack of resources ...
Testing:
1. Wrote simple tests as part of my implementation. a. crawl_test.py
b. crawl_facade_test.py
Prerequisites to run the server:
1. python 3.
2. postgres installed on the machine with at_bay db created.And init env var with
connection string ->
      "postgresql://postgres:password@localhost:5432/<db-name>".
3. Install requirements.txt file with pip -> pip install -r requirements.txt. (checked on mac)
