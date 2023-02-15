# Flux Query Builder

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

For most use cases the `InlineFunction` class is sufficent

## Fluid API

The FluxQuery class exposes all functions as own methods vie a metaclass. Unfortunetly Intellisense is not aware of the methods but if you prefer, instead of using the pipe operator you can use the fluid API

__Some functions in the flux langauge are python keywords because of this they are suffixed with a `_`__

__The query will still throw if the required parameters are not given!__


Example:

```py
q = (
	FluxQuery()
	.from_(bucket_name="bucket", start=S("-30m"))
	.filter(fn="(r) => r._measurement = 'meas'")
	.count()
)
```

## Reference

### FluxQuery

The querybuilder class. FluxQueries are __immutable__ every operation like piping a new function with `|` or even adding an import creates a clone of the class

#### Methods

### The `S` Utility Class

Some times you want to add parameters to functions you pipe and want them to be strings. In that case the S class is a wrapper to add qoutes to the string

For Example:

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
In this case the `fn` argument will be taken as is and the `S("30m")` will be in quoutes.

The rational behind this is that there still needs to be a way to add non string values

### FluxTime

Flux time is a utlility class to deal with flux durations and dates and pythons datetimes and timedeltas

#### Methods

TODO

### FilterBuilder

The FilterBuilder makes it easy building filters for your query by generating a InlineFunction that respects all the given conditions

#### Methods

TODO

