# conftest.py
import pytest
from flask import Flask
import os
import tempfile
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server import app


@pytest.fixture(scope="module")
def client():
    """Config client for test"""
    app.config["TESTING"] = True
    app.config["DEBUG"] = False

    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
