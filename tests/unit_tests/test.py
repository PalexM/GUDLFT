import pytest

# from server import loadClubs, loadCompetitions


class TestAppRoutes:
    @pytest.fixture
    def client(self, client):
        """Use fixture client defined in conftest.py."""
        return client

    def test_index_route(self, client):
        """Testing index route"""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Please enter your secretary email to continue:" in response.data

    def test_show_summary_route_ok(self, client):
        """Testing show summary route, test with correct email"""
        test_email = "john@simplylift.co"
        response = client.post("/showSummary", data={"email": test_email})
        assert response.status_code == 200
        assert b"Competitions:" in response.data

    def test_show_summary_route_ko(self, client):
        """Testing show summary route, test with incorrect email"""
        test_email = "john@simplylift.cqso"
        response = client.post("/showSummary", data={"email": test_email})
        assert response.status_code == 200
        assert b"Something went wrong" in response.data

    def test_book_competition_route_ok(self, client):
        """Testing booking competition with correct data"""
        competition_name = "Spring Festival"
        club_name = "Simply Lift"
        places_to_purchase = "3"
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_to_purchase,
            },
        )
        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data

    def test_book_competition_route_ko_url(self, client):
        """Testing booking competition with incorect url route"""
        competition_name = "Spring Festivale"
        club_name = "Simply Lifte"
        response = client.get(f"/book/{competition_name}/{club_name}")
        print(f" \n \n  response : \n {response.data} \n\n")
        assert response.status_code == 200
        assert b"Something went wrong" in response.data

    def test_book_competition_route_ko_surbooking(self, client):
        """Testing booking competition with incorect data, trying to book more than 12 places"""
        competition_name = "Spring Festival"
        club_name = "Simply Lift"
        places_to_purchase = "13"
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_to_purchase,
            },
        )
        assert response.status_code == 200
        assert b"Surbooking Error :" in response.data

    def test_purchase_places_error_zero(self, client):
        """Testing booking competition with incorect data, trying to book 0 place"""
        competition_name = "Spring Festival"
        club_name = "Simply Lift"
        places_to_purchase = "0"
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_to_purchase,
            },
        )
        assert response.status_code == 200
        assert b"Choice Error :" in response.data

    def test_dashboard(self, client):
        """Testing dashboard route and dashboard display"""
        response = client.get("/dashboard")
        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Clubs Dashboard" in response.data


# class TestLoadFunctions:
#     """Test load funtions presents in server file"""

#     def test_load_clubs(self):
#         """Test in load clubs load data correctly and if data exists"""
#         clubs = loadClubs()
#         assert clubs is not None
#         assert len(clubs) > 0

#     def test_load_competitions(self):
#         """Test in load clubs competitions data correctly and if data exists"""
#         competitions = loadCompetitions()
#         assert competitions is not None
#         assert len(competitions) > 0
