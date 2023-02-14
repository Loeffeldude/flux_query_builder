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

## Features

- Automatically resolves imports for used functions
- All Flux functions available via the functions module
- Flux functions throw errors if reqeuired parameters are not given 

## 