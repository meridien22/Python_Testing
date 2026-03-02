from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task(2)
    def home(self):
        """Site homepage."""
        self.client.get("/", name="Home page")

    @task(2)
    def connection_with_good_email(self):
        """Connection with a valid email address."""
        response = self.client.post(
            "/showSummary",
            {"email": "john@simplylift.co"},
            name="Good connection",
        )

    @task(1)
    def connection_with_bad_email(self):
        """Connection with an incorrect email address."""
        response = self.client.post(
            "/showSummary",
            {"email": "XXX@simplylift.co"},
            name="Bad connection",
        )

    @task(1)
    def connection_with_email_empty(self):
        """Connection with an empty email address."""
        response = self.client.post(
            "/showSummary",
            {"email": "XXX@simplylift.co"},
            name="Bad connection",
        )
    
    @task(1)
    def book_places_ok(self):
        """Reservation correct."""
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
        """Reservations for more than 12 places."""
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
        """Booking a number of places greater than the number of club points."""
        response = self.client.post(
            "/purchasePlaces",
            {
                "competition": "Spring Festival",
                "club": "Iron Temple",
                "places": "5",
            },
            name="Book places limit point",
        )

    @task(3)
    def display_public_page_with_points(self):
        """Display of the public page showing the clubs' points."""
        self.client.get("/points", name="Public page with points")