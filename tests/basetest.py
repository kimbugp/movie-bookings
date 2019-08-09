import pytest

from unittest import TestCase


class BaseTestCase():
    
    def assertEqual(self, arg1, arg2):
        assert arg1 == arg2
