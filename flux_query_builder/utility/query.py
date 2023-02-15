from typing import Any

class S:
    """Utility class to stringify a value for Query Functions

    Example Usage:
        `From(bucket_name=S("bucket-name"))`
    """
    value: Any

    def __init__(self, val) -> None:
        self.value = val
    
    def __str__(self) -> str:
        return f'"{self.value}"'

class FilterCondition:
    """Represents a filter condition for a filter function
    """
    record_field: str
    operator: str
    value: Any

    def __init__(self, record_field: str, operator: str, value: Any, other=None) -> None:
        self.record_field = record_field
        self.operator = operator
        self.value = value

    def __str__(self) -> str:
        return f"r.{self.record_field} {self.operator} {self.value}"

class FilterBuilder:
    """Creates a filter function with a inline for measurements, fields and tags
    """

    raw_inline: str
    AND = "and"
    OR = "or"

    def __init__(self) -> None:
        self.raw_inline = ""

    def add(self, condition: FilterCondition, connector=AND) -> "FilterBuilder":
        if self.raw_inline == "":
            self.raw_inline += f"({condition})"
        else:
            self.raw_inline += f" {connector} ({condition})"

        return self
    
    def __or__(self, other: "FilterBuilder") -> "FilterBuilder":
        return self.add(other, connector=self.OR)
    
    def __and__(self, other: "FilterBuilder") -> "FilterBuilder":
        return self.add(other, connector=self.AND)
    
    def __str__(self) -> str:
        return f"(r) => {self.raw_inline}"