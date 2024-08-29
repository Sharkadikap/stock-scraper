from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        # Run the scrape.py script
        result = subprocess.run(['python', 'scrape.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({"status": "success", "message": "Data scraping completed."}), 200
        else:
            return jsonify({"status": "error", "message": result.stderr}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
