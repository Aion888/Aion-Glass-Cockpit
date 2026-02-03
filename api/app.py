from flask import Flask, jsonify
import importlib.metadata as md

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/version")
def version():
    return jsonify(flask=md.version("flask"))

if __name__ == "__main__":
    # 0.0.0.0 is best for Codespaces port forwarding
    app.run(host="0.0.0.0", port=5001, debug=True)
