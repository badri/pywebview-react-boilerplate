import os
import threading
import webview
from app import app


def start_flask():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)


if __name__ == '__main__':
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Create pywebview window pointing to Flask server
    window = webview.create_window('Flask Hello World', 'http://127.0.0.1:5000')
    webview.start(debug=True)
