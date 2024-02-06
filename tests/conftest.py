# conftest.py
import pytest
from flask import Flask
import os
import tempfile
import json

from server import app


@pytest.fixture(scope="module")
def client():
    """Config client for test"""
    app.config["TESTING"] = True
    app.config["DEBUG"] = False

    # Configurarea unei baze de date temporare, dacă este necesar
    # db_fd, db_path = tempfile.mkstemp()
    # app.config['DATABASE'] = db_path

    # Initializare client de testare
    testing_client = app.test_client()

    # Contextul aplicației Flask este împins pentru ca testele să ruleze în contextul aplicației
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # aceasta permite executarea codului după finalizarea testului

    # Teardown
    ctx.pop()
    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture(scope="module")
def setup_clubs_competitions():
    """Create test data for clubs and competitions"""
    clubs = [
        {"name": "Test Club", "email": "test@club.com", "points": "100"},
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
    ]
    competitions = [
        {"name": "Test Competition", "date": "2023-12-31 10:00:00"},
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
    ]

    with open("test_clubs.json", "w") as clubs_file:
        json.dump({"clubs": clubs}, clubs_file)
    with open("test_competitions.json", "w") as competitions_file:
        json.dump({"competitions": competitions}, competitions_file)

    yield  # Acest yield nu returnează nimic, dar asigură rularea codului de teardown

    os.remove("test_clubs.json")
    os.remove("test_competitions.json")
