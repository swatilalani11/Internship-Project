from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# ---------- POST METHOD ----------
@app.route('/sma', methods=['POST'])
def calculate_sma_post():
    try:
        data = request.get_json()
        prices = data.get('prices')
        window = data.get('window')

        # Validation
        if not prices or not isinstance(prices, list):
            return jsonify({"error": "Invalid or missing 'prices'. Must be a list."}), 400
        if not isinstance(window, int) or window < 1:
            return jsonify({"error": "Invalid or missing 'window'. Must be integer >= 1."}), 400

        df = pd.DataFrame({'Price': prices})

        sma = []
        for i in range(len(df)):
            if i < window - 1:
                sma.append(None)
            else:
                sma.append(sum(df['Price'][i-window+1:i+1]) / window)
        df['SMA'] = sma

        return jsonify(df.to_dict(orient='records'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- GET METHOD ----------
@app.route('/', methods=['GET'])
def calculate_sma_get():
    try:
        prices = request.args.get('prices')  # comma-separated string
        window = request.args.get('window', type=int)

        if not prices or not window:
            return jsonify({"error": "Missing 'prices' or 'window' parameter"}), 400

        price_list = [float(p) for p in prices.split(',')]
        df = pd.DataFrame({'Price': price_list})

        sma = []
        for i in range(len(df)):
            if i < window - 1:
                sma.append(None)
            else:
                sma.append(sum(df['Price'][i-window+1:i+1]) / window)
        df['SMA'] = sma

        return jsonify(df.to_dict(orient='records'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
