from flask import Flask, request, send_from_directory, jsonify
import json
import os

# Initialize Flask and tell it the current directory ('.') is the static folder
app = Flask(__name__, static_folder='.')

# 1. Route for the Root (http://127.0.0.1:8000/)
# This replaces "python -m http.server" - it serves your files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# 2. THE FIX: Catch-all route for any other file (scripts, images, index.html)
# This mimics the "python -m http.server" behavior
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# 3. Your custom Save endpoint
@app.route('/save-presets', methods=['POST'])
def save_presets():
    try:
        with open('presets_backup.json', 'w') as f:
            json.dump(request.json, f, indent=4)
        return jsonify({"status": "Saved to presets_backup.json"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Setting debug=True is helpful; it restarts the server when you change code
    # app.run(port=8000)
    app.run(port=8000, debug=True)