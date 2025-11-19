from flask import Flask, render_template, jsonify, request
import os
import socket
import psutil
import datetime as dt

app = Flask(__name__)

START_TIME = dt.datetime.utcnow()
REQUEST_COUNT = 0


def get_uptime_seconds():
    delta = dt.datetime.utcnow() - START_TIME
    return int(delta.total_seconds())


@app.before_request
def count_request():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


@app.route("/")
def index():
    # Renders real-time dashboard UI
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/info")
def info():
    return jsonify(
        app="DevOps CI/CD Demo",
        version=os.getenv("APP_VERSION", "v1"),
        environment=os.getenv("APP_ENV", "dev"),
        host=socket.gethostname(),
        client_ip=request.remote_addr,
    )


@app.route("/api/status")
def api_status():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    uptime = get_uptime_seconds()

    return jsonify(
        time=dt.datetime.utcnow().isoformat() + "Z",
        cpu_percent=cpu,
        memory_percent=mem,
        uptime_seconds=uptime,
        requests=REQUEST_COUNT,
        host=socket.gethostname(),
        version=os.getenv("APP_VERSION", "v1"),
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
