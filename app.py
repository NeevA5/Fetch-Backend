from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Global variable to track total p across all payers
total_points = 0

# Dictionary to store each payer's current balance, e.g., {"DANNON": {"points": 1000}}
payers = {}

# List to store all transactions in the format {"payer": str, "points": int, "timestamp": str}
transactions = []

# Home route that provides a simple summary of the total points available
@app.route("/")
def home():
    return "Hello! You currently have " + str(total_points) + " points. (Refresh this page to reflect transactions)"

# Add route for adding points
# Expects a JSON request with "payer", "points", and "timestamp" fields
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    global total_points

    # Ensure data isn't null as basic error handling
    if data:
        # Extract relevant fields from the request body
        payer = data.get("payer")
        points = data.get("points")
        timestamp = data.get("timestamp")

        # Update the total points tracker
        total_points += points
        
        # Either add the payer as a new payer or update their current points
        if payer in payers:
            payers[payer]["points"] += points
        else:
            payers[payer] = {"points": points}
        
        # Add the transaction to the list
        transactions.append({"payer": payer, "points": points, "timestamp": timestamp})
        return '', 200 


# Spend route for making purchases based on transaction order
# Expects a JSON request with a "points" field specifying the amount to spend
@app.route("/spend", methods=["POST"])
def spend():
    data = request.get_json()
    global total_points
    
    # Ensure data isn't null as basic error handling
    if data:
        toSpend = data.get("points")
        
        # Verifies user has enough points to make the requested purchase, returns error code and message otherwise.
        if(toSpend > total_points):
            return "You don't have enough points to spend that much!", 400
        
        # Points_spent dictionary used for outputting response body
        points_spent = {}

        # Sort transactions by timestamp in case add requests are made out of timestamp order
        transactions.sort(key=lambda x: datetime.fromisoformat(x["timestamp"].replace("Z", "+00:00")))

        # Process each transaction, deducting points until the requested amount is spent
        for transaction in transactions:

            # End the loop if the request spending amount has been met to stop unneccesary iterations
            if toSpend == 0:
                break
            
            current_payer = transaction["payer"]
            current_points = transaction["points"]

            # Determine whether to deduct all points fron the user or only the amount left to spend
            deduct = min(toSpend, current_points)

            # Update the amount left to spend
            toSpend -= deduct
            
            # Update the global total points tracker
            total_points -= deduct

            # Update the points in the current payer's balance
            payers[current_payer]["points"] -= deduct

            # Add the payer to the points_spent dictionary with default value 0 if they are not in it
            if not current_payer in points_spent:
                points_spent[current_payer] = 0

            # Deducts the amount spent from relevant payer for negative output
            points_spent[current_payer] -= deduct
        
        # Convert points_spent dictionary into expected response body format
        output = [{"payer": payer, "points": points_spent[payer]} for payer in points_spent]
        return jsonify(output), 200

# Balance route for outputting current payer balances
@app.route("/balance", methods=["GET"])
def balance():
    # Convert payer dictionary into expected response body format
    balances = {payer: payers[payer]["points"] for payer in payers}
    return jsonify(balances), 200

if __name__ == '__main__':
    # Run the API on port 8000
    app.run(debug=True, port = 8000)
