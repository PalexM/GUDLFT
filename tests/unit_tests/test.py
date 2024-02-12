import pytest


def update_club_points(clubs, club_name, points_to_deduct):
    for club in clubs:
        if club["name"] == club_name:
            club["points"] = str(int(club["points"]) - points_to_deduct)
            break
    return clubs


def update_competition_places(competitions, competition_name, places_required):
    for competition in competitions:
        if competition["name"] == competition_name:
            competition["numberOfPlaces"] = str(
                int(competition["numberOfPlaces"]) - places_required
            )
            break
    return competitions


def test_update_club_and_competition():
    clubs_data = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]
    competitions_data = [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13",
        },
    ]

    updated_clubs = update_club_points(clubs_data, "Simply Lift", 3)
    updated_club = next(club for club in updated_clubs if club["name"] == "Simply Lift")

    updated_competitions = update_competition_places(
        competitions_data, "Spring Festival", 3
    )
    updated_competition = next(
        competition
        for competition in updated_competitions
        if competition["name"] == "Spring Festival"
    )

    assert (
        updated_club["points"] == "10"
    ), f"Expected points to be '10', got {updated_club['points']}"
    assert (
        updated_competition["numberOfPlaces"] == "22"
    ), f"Expected number of places to be '22', got {updated_competition['numberOfPlaces']}"
