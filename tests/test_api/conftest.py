import subprocess
import time
import sys
import os
import socket

import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/palindrome"


@pytest.fixture
def generate_sample_string():
    """
    Fixture to generate a sample string for testing retrieval.
    :return: A dictionary with the generated string's `id` and `result`.
    """
    response = requests.post(f"{BASE_URL}/generate-string", json={"palindrome": True, "length": 6})
    data = response.json()
    return {"id": data["id"], "result": data["result"]}


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


@pytest.fixture(scope="session", autouse=True)
def start_flask_app():
    """
    Start the Flask app for testing. Skip starting if already running or inside Docker.
    """
    port = 5000
    app_process = None

    if not os.getenv("DOCKER"):
        if not is_port_in_use(port):
            app_process = subprocess.Popen(["run-palindrome"])
            time.sleep(3)
        else:
            print(f"Flask app already running on port {port}, skipping startup.")

    yield

    if app_process:
        app_process.terminate()
        app_process.wait()


