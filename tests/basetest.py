import pytest
from apps.middlewares.validation import ValidationError
from unittest import TestCase
from sql import get_cte_query


class BaseTestCase():

    def assertEqual(self, arg1, arg2):
        assert arg1 == arg2

    def test_file_not_found(self):
        with pytest.raises(ValidationError) as error:
            get_cte_query('invsf')
