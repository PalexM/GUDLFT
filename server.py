import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    """Load clubs from clubs.json file"""
    with open("clubs.json") as c:
        clubs_list = json.load(c)["clubs"]
        return clubs_list


def load_competitions():
    """Load competitions from competitions.json file"""
    with open("competitions.json") as comps:
        competitions_list = json.load(comps)["competitions"]
        return competitions_list


app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()


@app.route("/")
def index():
    """Home page"""
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    """Competitions summary"""
    club = [club for club in clubs if club["email"] == request.form["email"]]
    try:
        club = club.pop()
    except IndexError:
        return render_template(
            "index.html",
            error_message="No secretary find with this email, try again or contact your club!",
        )
    if club:
        return render_template("welcome.html", club=club, competitions=competitions)
    else:
        error_message = (
            "No secretary find with this email, try again or contact your club!"
        )
        return render_template("index.html", error_message=error_message)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    """Booking competitions page"""
    found_club = [c for c in clubs if c["name"] == club]
    found_competition = [c for c in competitions if c["name"] == competition]
    try:
        found_club = found_club.pop()
        found_competition = found_competition.pop()
    except IndexError as e:
        return render_template(
            "index.html", error_message=f"Something went wrong : {e}"
        )
    if found_club and found_competition["date"] > str(datetime.now()):
        return render_template(
            "booking.html", club=found_club, competition=found_competition
        )
    else:
        error_message = "To late, inscriptions are closed !"
        return render_template(
            "welcome.html",
            club=found_club,
            competition=found_competition,
            error_message=error_message,
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    """Purchaise booked places"""
    competition = [c for c in competitions if c["name"] == request.form["competition"]]
    club = [c for c in clubs if c["name"] == request.form["club"]]
    places_required = int(request.form["places"]) if request.form["places"] != "" else 0
    print(places_required)
    try:
        competition = competition.pop()
        club = club.pop()
    except IndexError as e:
        return render_template(
            "index.html", error_message=f"Error : Something went wrong : {e}"
        )
    error_message = None
    if places_required > int(club["points"]):
        error_message = "Surbooking Error : You try to book more places than you have available points!"
    elif places_required > int(competition["numberOfPlaces"]):
        error_message = (
            "Surbooking Error : You try to book more than there are available places!"
        )
    elif places_required > 12:
        error_message = "Surbooking Error : You can not book more than 12 places!"
    elif places_required <= 0:
        error_message = "Choice Error : Please chose a number between 1 and 12!"

    if not error_message:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - places_required
        )
        club["points"] = int(club["points"]) - places_required
        flash("Great-booking complete!")
        return render_template("welcome.html", club=club, competitions=competitions)
    else:
        return render_template(
            "welcome.html",
            club=club,
            competitions=competitions,
            error_message=error_message,
        )


@app.route("/dashboard")
def dashboard():
    """Clubs points dashboard"""
    return render_template("dashboard.html", clubs=clubs)


@app.route("/logout")
def logout():
    """Logout route"""
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
