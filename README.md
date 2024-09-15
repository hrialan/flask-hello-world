# Flask MySQL Example

This is a simple hello world application using Flask.

### Prerequisites
- Python 3.x
- Flask
- mysql-connector-python

### How to run the application

1. Clone the repository
2. Setup the Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```
3. Set the environment variables
```sh
export MYSQL_HOST="localhost"
export MYSQL_USER="root"
export MYSQL_PASSWORD="password"
export MYSQL_DATABASE="test"
```
4. Run the following command to install the dependencies
```
pip install -r requirements.txt
```
5. Run the following command to start the application
```
python app.py
```
6. Open the browser and navigate to `http://localhost:8080/`

### Endpoints

#### Root Endpoint
- URL: /
- Method: GET
- Description: Returns a simple "Hello World!" message.

#### Fake Data Endpoint
- URL: /api/v1/fake-data
- Method: GET
- Description: Returns a JSON object with fake data.


#### Test MySQL Endpoint
- URL: /api/v1/test-mysql
- Method: GET
- Description: Checks the MySQL connection and retrieves data from the test_table.

### Test the application

1. Install Pytest
```
pip install pytest
```
2. Run the following command to run the tests
```
python test_app.py
```

