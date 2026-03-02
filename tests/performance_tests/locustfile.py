from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task(2)
    def home(self):
        self.client.get("/", name="Home page")

    @task(2)
    def good_connection(self):
        response = self.client.post(
            "/showSummary",
            {"email": "john@simplylift.co"},
            name="Good connection",
        )

    @task(1)
    def bad_connection(self):
        response = self.client.post(
            "/showSummary",
            {"email": "XXX@simplylift.co"},
            name="Bad connection",
        )
    
    @task(1)
    def book_places_ok(self):
        response = self.client.post(
            "/purchasePlaces",
            {
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "5",
            },
            name="Book places ok",
        )
    
    @task(1)
    def book_places_limit_12(self):
        response = self.client.post(
            "/purchasePlaces",
            {
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "13",
            },
            name="Book places limit 12",
        )

    @task(1)
    def book_places_limit_point(self):
        response = self.client.post(
            "/purchasePlaces",
            {
                "competition": "Spring Festival",
                "club": "Iron Temple",
                "places": "5",
            },
            name="Book places limit point",
        )