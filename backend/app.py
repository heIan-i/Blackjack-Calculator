from flask import Flask, jsonify, request
from flask_cors import CORS  # allows React frontend to call API

app = Flask(__name__)
CORS(app)  # enable CORS for all routes (for development)

# Hidden Python code stored in the server
def secret_function(user_input: str) -> str:
    # Any hidden logic goes here
    return f"Server processed hidden Python code with input: {user_input}"

@app.route("/run", methods=["POST"])
def run_hidden_code():
    data = request.get_json()
    user_input = data.get("input", "")
    try:
        result = secret_function(user_input)
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)