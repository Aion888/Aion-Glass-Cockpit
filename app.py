from pm_app.app import app

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=True, use_reloader=False)
