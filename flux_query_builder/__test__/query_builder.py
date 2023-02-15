from flux_query_builder.builder import FluxQuery
from flux_query_builder.utility import S
import flux_query_builder.functions as fn
import flux_query_builder.functions.aggregate as agg
import flux_query_builder.functions.mqtt as mqtt
import unittest


class QueryBuilderTest(unittest.TestCase):
    def test_pipe_fn(self):
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
|> aggregate.rate(every: "1m")
""",
        )

    def test_add_import_without_function(self):
        q = FluxQuery()
        q = q.import_package("mqtt")

        q = q | fn.From(bucket=S("test"), start=S("2021-01-01T00:00:00Z"))

        self.assertEqual(
            q.get_query(),
            """import "mqtt"
from(bucket: "test", start: "2021-01-01T00:00:00Z")
""",
        )

    def test_pipe_query(self):
        q = FluxQuery()
        q = (
            q
            | fn.From(bucket=S("test"), start=S("2021-01-01T00:00:00Z"))
            | fn.Count()
            | agg.Rate(every=S("1m"))
        )

        q2 = FluxQuery()
        q2 = (
            q2
            | fn.Count()
            | mqtt.Publish(
                broker=S("mqtt://example.com"), topic=S("test"), message=S("test")
            )
        )

        q = q | q2

        self.assertEqual(
            q.get_query(),
            """import "aggregate"
import "mqtt"
from(bucket: "test", start: "2021-01-01T00:00:00Z")
|> count()
|> aggregate.rate(every: "1m")
|> count()
|> mqtt.publish(broker: "mqtt://example.com", topic: "test", message: "test")

""",
        )

    def test_immutability_pipe(self):
        q = FluxQuery()
        q2 = (
            q
            | fn.From(bucket=S("test"), start=S("2021-01-01T00:00:00Z"))
            | fn.Count()
            | agg.Rate(every=S("1m"))
        )

        q = q | fn.Count()

        self.assertEqual(
            q.get_query(),
            """count()
""",
        )

        self.assertEqual(
            q2.get_query(),
            """import "aggregate"
from(bucket: "test", start: "2021-01-01T00:00:00Z")
|> count()
|> aggregate.rate(every: "1m")
""",
        )

    def test_fn_method_expose(self):
        q = FluxQuery()

        q = (
            q.from_(bucket=S("test"), start=S("2021-01-01T00:00:00Z"))
            .aggregate_rate(every=S("1m"))
            .count()
        )

        self.assertEqual(
            q.get_query(),
            """import "aggregate"
from(bucket: "test", start: "2021-01-01T00:00:00Z")
|> aggregate.rate(every: "1m")
|> count()
""",
        )
