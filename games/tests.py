from django.test import TestCase
from django.contrib.auth.models import User

from .models import Game


class GameTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a game 
        test_game = Game.objects.create(
            player=testuser1, title='game title', description='description content...')
        test_game.save()

    def test_game_content(self):
        game = Game.objects.get(id=1)
        expected_player = f'{game.player}'
        expected_title = f'{game.title}'
        expected_description = f'{game.description}'
        self.assertEqual(expected_player, 'testuser1')
        self.assertEqual(expected_title, 'game title')
        self.assertEqual(expected_description, 'description content...')