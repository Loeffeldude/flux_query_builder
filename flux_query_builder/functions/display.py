from flux_query_builder.functions.base import FluxQueryFunction

class Display(FluxQueryFunction):
    """display() returns the Flux literal representation of any value as a string.Basic types are converted directly to a string.
Bytes types are represented as a string of lowercase hexadecimal characters prefixed with 0x.
Composite types (arrays, dictionaries, and records) are represented in a syntax similar
to their equivalent Flux literal representation.Note the following about the resulting string representation:display() differs from string() in that display() recursively converts values inside
composite types to strings. string() does not operate on composite types.(Required)
Value to convert for display.Use array.from() and display() to quickly observe any value.

    Params:
        
        v 
        - (Required)
Value to convert for display.
        
    """
    name = "display"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )