from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

expiry_days = {
    "NIFTY": 3,      # Thursday
    "BANKNIFTY": 2,  # Wednesday
    "FINNIFTY": 1    # Tuesday
}

def calculate_expiry(index, date_str):
    given_date = datetime.strptime(date_str, "%Y-%m-%d")
    expiry_weekday = expiry_days[index]
    current_weekday = given_date.weekday()

    if current_weekday > expiry_weekday:
        days_to_add = 7 - (current_weekday - expiry_weekday)
    else:
        days_to_add = expiry_weekday - current_weekday

    expiry_date = given_date + timedelta(days=days_to_add)
    return expiry_date.strftime("%Y-%m-%d")

@app.route("/expiry", methods=["GET", "POST"])
def expiry():
    try:
        if request.method == "POST":
            data = request.get_json()
            index = data.get("index", "").upper()
            date_str = data.get("date")
        else:  # GET method
            index = request.args.get("index", "").upper()
            date_str = request.args.get("date")

        if not index or not date_str:
            return jsonify({"error": "Missing index or date parameter"}), 400

        if index not in expiry_days:
            return jsonify({"error": "Index not found"}), 400

        expiry_date = calculate_expiry(index, date_str)
        return jsonify({
            "index": index,
            "input_date": date_str,
            "expiry_date": expiry_date
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Running on port 5006")
    app.run(debug=True, port=5006)
