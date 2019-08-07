import pytest

from unittest import TestCase


@pytest.mark.usefixtures("base_test_case")
class BaseTestCase(TestCase):
    pass
