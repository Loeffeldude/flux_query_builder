# Flux Query Builder

Version: 1.0.0


A python querybuilder for the flux query language used by InfluxDB

## Getting Started

### Installation

```shell
$ pip install flux-query-builder
 ```

 ### Building Queries

 ```py
from flux_query_builder import FluxQuery
from flux_query_builder.utility import S
import flux_query_builder.functions as fn
	
q = (
	FluxQuery() 
	| fn.From(bucket=S("bucket-name")) 
	| fn.Range(start=S("-1d"))
	| fn.AggregateWindow(every=S("30m"),fn=fn.Mean)
)

print(q.get_query())
```

Expected Output:

```flux
from(bucket:"bucket-name")
|> range(start: "-1d")
|> aggregateWindow(every: "30m", fn: mean)
```


## Creating your custom Functions

It is sometimes usefull to create and save a custom function for later use

For most use cases the `InlineFn` class is sufficent if you want to do something more custom you can inherit the `FluxQueryFunction` class. 

```py
from flux_query_builder.functions.base import FluxQueryFunction
from flux_query_builder.functions import InlineFn

class MeasurementFilter(FluxQueryFunction):

    name = "measurementFilter"
    package=None

    def __init__(self, measurement ):
            super().__init__(measurement=measurement)

    def __str__(self) -> str:
        return f"(r) => r._measurement == \"{self.params.get('measurement')}\")"

```

## Fluid API

The FluxQuery class exposes all functions as it's own methods via a metaclass. Unfortunetly Intellisense is not aware of the methods but if you prefer, instead of using the pipe operator, you can use the Fluid API

__Some functions in the flux langauge are python keywords because of this they are suffixed with a `_`__

__The query will still throw if the required parameters are not given!__


Example:

```py
q = (
	FluxQuery()
	.from_(bucket="bucket", start=S("-30m"))
	.filter(fn="(r) => r._measurement = 'meas'")
	.count()
)
```

## Reference

### FluxQuery

The querybuilder class. FluxQueries are __immutable__ every operation like piping a new function with `|` or even adding an import creates a clone of the class

### The `S` Utility Class

Some times you want to add parameters to functions you pipe and want them to be strings. In that case the S class is a wrapper to add qoutes to the string

Example:

```py
from flux_query_builder import FluxQuery
from flux_query_builder.utility import S
import flux_query_builder.functions as fn

q = FluxQuery()

q = (
	q 
	| fn.Filter(fn="(r) => r._measurement = 'meas'")
	| fn.AggregateWindow(every=S("30m"),fn=fn.Mean)
)
```

Expected Output:

```flux
from(bucket:"bucket-name")
|> range(start: "-1d")
|> aggregateWindow(every: "30m", fn: mean)
```

In this case the `fn` argument will be taken as is and the `S("30m")` will be in quoutes.

The rational behind this is that there still needs to be a way to add non string values


### InlineFn

A Utility class for creating inline functions like those in the filter function

Example:

```py
from flux_query_builder.functions import InlineFn
from flux_query_builder import FluxQuery
from flux_query_builder.utility import S
# Create a function that filters out all measurements that are not "meas"
meas_filter = InlineFn("r", "r._measurement == 'meas'")
print(meas_filter)

q = FluxQuery(bucket_name="bucket-name", start=S("-1d")) | fn.Filter(fn=meas_filter)

print(q.get_query())
```

Expected Output:

```flux
(r) => r._measurement == 'meas'

from(bucket:"bucket-name", start: "-1d")
|> filter(fn: (r) => r._measurement == 'meas')
```

### FluxTime

Flux time is a utlility class to deal with flux durations and dates and pythons datetimes and timedeltas

Example:

```py
from flux_query_builder.utility import FluxTime

# Create a flux duration
duration = FluxTime(duration="1d")
print(duration)


# Create a flux duration from a timedelta
duration = FluxTime(duration=timedelta(days=1))
print(duration)

# Create a flux date from a datetime
date = FluxTime(date=datetime(2020,1,1))
print(date)
```

Expected Output:

```flux
1d
1d
2020-01-01T00:00:00Z
```


### FilterBuilder

The FilterBuilder makes it easy building filters for your query by generating a InlineFunction that respects all the given conditions

Example:

```py
from flux_query_builder import FluxQuery
from flux_query_builder.utility import S
from flux_query_builder.functions import FilterBuilder
import flux_query_builder.functions as fn

q = FluxQuery(bucket_name="bucket-name", start=S("-1d"))

# Create a filter that filters out all measurements that are not "meas" and all fields that are not "field"
build_filter = FilterBuilder().measurement("meas").field("field").build()

q = q | fn.Filter(fn=build_filter)
```

Expected Output:

```flux
from(bucket:"bucket-name", start: "-1d")
|> filter(fn: (r) => r._measurement == 'meas' and r._field == 'field')
```
