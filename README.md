# Fetch-Backend

This is a simple API built using Flask that allows you to manage points, track transactions, and spend points.

In order to run the application, it is necessary to have Python and the relevant libraries installed. Follow the steps below to set up and run the Flask application.


# Check if Python is installed on your device

Try the following commands in your terminal to see if Python is installed on your device
“python --version”
“python3 --version”

If Python is installed, the terminal should output a response similar to:

“Python 3.13.0”

If Python is not installed, go to “https://www.python.org/downloads/” to install the latest version.


# Create a virtual environment

A virtual environment will allow you to create a custom environment to download the necessary libraries to run the API without affecting any other Python projects. Run the following command in the folder containing the application to create a virtual environment called “venv”:

Windows: “python -m venv venv”
Mac/Linux: “python3 -m venv venv”


# Activate the virtual environment

Once the virtual environment has been created, use the following command to activate the virtual environment:

Windows: “.\venv\Scripts\activate”
Mac/Linux: source venv/bin/activate

Once activated, your terminal prompt should indicate the active virtual environment, as shown below:

(venv) $


# Install the required libraries

Inside the virtual environment, run the following command to install the necessary libraries defined in the pre-defined requirements.txt file:


“pip install -r requirements.txt”

# Run the application

Once the required libraries are installed, run the following command in order to launch the application:

“python app.py”

Once the application is running, the terminal should output a message similar to the following indicating that the application is successfully running on port 8000:

“* Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)”


# Use endpoints to conduct transactions

Using an HTTP client such as Postman or cURL, send transaction requests on the following routes:

GET -  http://127.0.0.1:8000/balance
This route returns a JSON response body that allows the API user to view the current balances for each payer who has conducted a transaction relevant to the user’s account.

POST -  http://127.0.0.1:8000/add
This route allows the API user to add (or remove) points from the current user’s account from a new or existing payer. It requires a JSON body of the following format:

{
"payer" : "DANNON",
"points" : 5000,
"timestamp" : "2020-11-02T14:00:00Z"
}

POST - http://127.0.0.1:8000/spend
This route allows the API user to spend a specified amount of points from the current user’s balance (provided that they have sufficient points in their balance). It requires a JSON body of the following format:

{"points" : 5000}


# Deactivate the application and virtual environment

Once you are done using the application, return to the terminal and input “CTRL-C” to terminate the application. In order to exit the virtual environment, input the following command into the terminal:

“deactivate”

The terminal prompt will return to its original state, indicating the virtual environment is no longer active.
