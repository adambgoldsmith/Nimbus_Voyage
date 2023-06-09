"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.board import create_events_list


class TestCreateEventsList(TestCase):
    def test_create_events_list_five_by_five(self):
        expected_value = ['chest', 'chest', 'nymph', 'nymph', 'shop', 'shop', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                          'empty', 'empty']
        self.assertEqual(expected_value, create_events_list(5, 5))

    def test_create_events_list_six_by_six(self):
        expected_value = ['chest', 'chest', 'nymph', 'nymph', 'shop', 'shop', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                          'empty', 'empty', 'empty', 'empty', 'empty', 'empty']
        self.assertEqual(expected_value, create_events_list(6, 6))
