from django.test import TestCase

from theatre.models import Play


class PlayModelTests(TestCase):
    def test_play_str(self):
        play = Play.objects.create(title="Test title")

        self.assertEqual(str(play), play.title)
