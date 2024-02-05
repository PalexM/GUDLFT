import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    """Home page"""
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]]
    try:
        club = club.pop()
    except IndexError:
        club = None
        return render_template("index.html", error_message="Something went wrong")
    if club:
        return render_template("welcome.html", club=club, competitions=competitions)
    else:
        error_message = (
            "No secretary find with this email, try again or contract your club!"
        )
        return render_template("index.html", error_message=error_message)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club]
    foundCompetition = [c for c in competitions if c["name"] == competition]
    if foundClub and foundCompetition[0]["date"] > str(datetime.now()):
        return render_template(
            "booking.html", club=foundClub[0], competition=foundCompetition[0]
        )
    else:
        error_message = "To late, inscriptions are closed !"
        return render_template(
            "welcome.html",
            club=foundClub[0],
            competition=foundCompetition[0],
            error_message=error_message,
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]]
    club = [c for c in clubs if c["name"] == request.form["club"]]
    placesRequired = int(request.form["places"])
    error_message = None
    if placesRequired > int(club[0]["points"]):
        error_message = "You try to book more places than you have available points!"
    if placesRequired > int(competition[0]["numberOfPlaces"]):
        error_message = "You try to book more than there are available places!"
    if placesRequired > 12:
        error_message = "You can not book more than 12 places!"
    if placesRequired == 0:
        error_message = "Please chose a number between 1 and 12!"

    if not error_message:
        competition[0]["numberOfPlaces"] = (
            int(competition[0]["numberOfPlaces"]) - placesRequired
        )
        club[0]["points"] = int(club[0]["points"]) - placesRequired
        flash("Great-booking complete!")
        return render_template(
            "welcome.html", club=club[0], competitions=competitions[0]
        )
    else:
        return render_template(
            "welcome.html",
            club=club[0],
            competitions=competitions[0],
            error_message=error_message,
        )


@app.route("/dashboard")
def dashboard():
    """Home page"""
    return render_template("dashboard.html", clubs=clubs)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
