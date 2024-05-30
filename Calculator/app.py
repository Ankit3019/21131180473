from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers/<number_id>', methods=['GET'])
def get_numbers(number_id):
    url = f'http://20.244.56.144/test/{number_id}'
    response = requests.get(url)
    if response.status_code == 200:
        numbers = response.json().get('numbers', [])
        average = sum(numbers) / len(numbers) if numbers else 0
        return jsonify({
            "windowPrevState": [],
            "windowCurrState": numbers[:10],
            "numbers": numbers,
            "avg": round(average, 2)
        }), 200
    return jsonify({"error": "Failed to fetch numbers"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
