from django.test import TestCase

from theatre.models import Genre


class GenreModelTests(TestCase):
    def test_genre_str(self):
        genre = Genre.objects.create(name="Test name")

        self.assertEqual(str(genre), genre.name)
