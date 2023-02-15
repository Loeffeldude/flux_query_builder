import unittest
from flux_query_builder.utility.query import FilterBuilder


class FilterBuilderTest(unittest.TestCase):
    def test_add_measurement(self):
        f = FilterBuilder()
        f = f.measurement("test").build()

        self.assertEqual(str(f), f'(r) => r._measurement == "test"')

    def test_add_tag(self):
        f = FilterBuilder()
        f = f.tag("test", "test")

        self.assertEqual(str(f), f'(r) => r.test == "test"')

    def test_add_field(self):
        f = FilterBuilder()
        f = f.field("test").build()

        self.assertEqual(str(f), f'(r) => r._field == "test"')

    def test_add_multiple(self):
        f = FilterBuilder()
        f = f.measurement("test").tag("test", "test").field("test").build()

        self.assertEqual(
            str(f),
            f'(r) => r._measurement == "test" and r.test == "test" and r._field == "test"',
        )

    def test_add_multiple_with_operator(self):
        f = FilterBuilder()
        f = (
            f.measurement("test")
            .tag("test", "test")
            .field("test", operator="or")
            .build()
        )

        self.assertEqual(
            str(f),
            f'(r) => r._measurement == "test" and r.test == "test" or r._field == "test"',
        )

    def test_brackets(self):
        f = FilterBuilder()
        f = (
            f.measurement("test")
            .start_bracket(operator=f.OR)
            .tag("test", "test")
            .field("test")
            .end_bracket()
            .build()
        )

        self.assertEqual(
            str(f),
            f'(r) => r._measurement == "test" or (r.test == "test" and r._field == "test")',
        )

    def test_nested_brackets(self):
        f = FilterBuilder()
        f = (
            f.measurement("test")
            .start_bracket(operator=f.OR)
            .tag("test", "test")
            .start_bracket()
            .field("test")
            .end_bracket()
            .end_bracket()
            .build()
        )

        self.assertEqual(
            str(f),
            f'(r) => r._measurement == "test" or (r.test == "test" and (r._field == "test"))',
        )

    def test_nested_brackets_end_to_end(self):
        f = FilterBuilder()
        f = (
            f.measurement("test")
            .start_bracket(operator=f.OR)
            .start_bracket()
            .tag("test", "test")
            .end_bracket()
            .start_bracket()
            .field("test")
            .end_bracket()
            .end_bracket()
            .build()
        )

        self.assertEqual(
            str(f),
            f'(r) => r._measurement == "test" or ((r.test == "test") and (r._field == "test"))',
        )
