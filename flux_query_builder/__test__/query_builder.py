from flux_query_builder.builder import FluxQuery
from flux_query_builder.utility import S
import flux_query_builder.functions as fn
import flux_query_builder.functions.aggregate as agg
import unittest


class QueryBuilderTest(unittest.TestCase):
    def test_pip_fn(self):
        q = FluxQuery()

        q = q | fn.From(bucket=S("test"), start=S("2021-01-01T00:00:00Z")) | fn.Count()

        self.assertEqual(
            q.get_query(),
            """from(bucket: "test", start: "2021-01-01T00:00:00Z")
|> count()
""",
        )

    def test_add_imports(self):
        q = FluxQuery()
        q = (
            q
            | fn.From(bucket=S("test"), start=S("2021-01-01T00:00:00Z"))
            | fn.Count()
            | agg.Rate(every=S("1m"))
        )

        self.assertEqual(
            q.get_query(),
            """import "aggregate"
from(bucket: "test", start: "2021-01-01T00:00:00Z")
|> count()
|> aggregate.rate(every: 1m)
""",
        )

    
