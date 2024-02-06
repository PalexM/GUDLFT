import pytest


class TestAppRoutes:
    @pytest.fixture
    def client(self, client):
        """Folosește fixture-ul client definit în conftest.py."""
        return client

    def test_index_route(self, client):
        """Testează dacă ruta index se încarcă corect."""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Please enter your secretary email to continue:" in response.data

    def test_show_summary_route_ok(self, client):
        """Testează afișarea sumarului pentru un email existent."""
        test_email = "john@simplylift.co"
        response = client.post("/showSummary", data={"email": test_email})
        assert response.status_code == 200
        assert b"Competitions:" in response.data

    def test_show_summary_route_ko(self, client):
        """Testează afișarea sumarului pentru un email existent."""
        test_email = "john@simplylift.cqso"
        response = client.post("/showSummary", data={"email": test_email})
        assert response.status_code == 200
        assert b"Something went wrong" in response.data

    def test_book_competition_route_ko(self, client):
        competition_name = "Spring Festivale"
        club_name = "Simply Lifte"
        response = client.get(f"/book/{competition_name}/{club_name}")
        print(f" \n \n  response : \n {response.data} \n\n")
        assert response.status_code == 200
        assert b"Something went wrong" in response.data

    def test_purchase_places_success(self, client):
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


# class TestLoadFunctions:
#     def test_load_clubs(self):
#         """Testează funcția loadClubs pentru a verifica încărcarea corectă a datelor."""
#         clubs = loadClubs()
#         assert clubs is not None
#         assert len(clubs) > 0  # Verifică dacă există cluburi încărcate

#     def test_load_competitions(self):
#         """Testează funcția loadCompetitions pentru a verifica încărcarea corectă a datelor."""
#         competitions = loadCompetitions()
#         assert competitions is not None
#         assert len(competitions) > 0  # Verifică dacă există competiții încărcate


# # Adaugă mai multe clase și teste după necesități
