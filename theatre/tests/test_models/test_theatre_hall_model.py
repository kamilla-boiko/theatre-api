from django.test import TestCase

from theatre.models import TheatreHall


class TheatreHallModelTests(TestCase):
    def test_theatre_hall_str(self):
        theatre_hall = TheatreHall.objects.create(
            name="Test name", rows=10, seats_in_row=10
        )

        self.assertEqual(str(theatre_hall), theatre_hall.name)

    def test_theatre_hall_capacity(self):
        theatre_hall = TheatreHall.objects.create(
            name="Test name", rows=10, seats_in_row=10
        )

        self.assertEqual(theatre_hall.capacity, 100)
