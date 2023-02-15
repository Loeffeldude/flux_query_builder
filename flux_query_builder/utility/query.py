from typing import Any

from flux_query_builder.functions.inline import InlineFn

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

class FilterBuilder:
    """Creates a filter function with a inline for measurements, fields and tags

    Example Usage:
        `FilterBuilder().measurement("cpu").field("usage_user").build()`

    """

    raw_inline: str
    AND = "and"
    OR = "or"

    def __init__(self) -> None:
        self.raw_inline = ""

    def build(self) -> "InlineFn":
        """Builds the filter function

        Returns:
            InlineFn: The resuting filter function
        """
        return InlineFn(fn=str(self))
    
    def start_bracket(self, operator=AND) -> "FilterBuilder":
        """Adds a start bracket to the filter function. Returns a new instance of FilterBuilder

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = self.clone()
        clone._add_to_raw(operator, "(")
        return clone

    def end_bracket(self) -> "FilterBuilder":
        """Adds a end bracket to the filter function. Returns a new instance of FilterBuilder

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = self.clone()
        clone.raw_inline += ")"
        return clone

    def measurement(self, measurement_val: str, operator=AND) -> "FilterBuilder":
        """Adds a measurement filter to the filter function. Returns a new instance of FilterBuilder

        Args:
            measurement_val (str): the value of the measurement to filter on
            operator (_type_, optional): The operator to join with. Defaults to AND.

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = self.clone()
        clone._add_to_raw(operator, f'r._measurement == {S(measurement_val)}')
        return clone
    
    def field(self, field_val: str, operator=AND) -> "FilterBuilder":
        """Adds a field filter to the filter function. Returns a new instance of FilterBuilder

        Args:
            field_val (str): the value of the field to filter on
            operator (_type_, optional): The operator to join with. Defaults to AND.

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = self.clone()
        clone._add_to_raw(operator, f'r._field == {S(field_val)}')
        return clone
    
    def tag(self, tag: str, tag_val: str, operator=AND) -> "FilterBuilder":
        """Adds a tag filter to the filter function. Returns a new instance of FilterBuilder

        Args:
            tag (str): The tag to filter on
            tag_val (str): The value of the tag to filter on
            operator (_type_, optional): The operator to join with. Defaults to AND.

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = self.clone()
        clone._add_to_raw(operator, f'r.{tag} == {S(tag_val)}')
        return clone

    def clone(self) -> "FilterBuilder":
        """Creates a clone of the FilterBuilder

        Returns:
            FilterBuilder: a new instance of FilterBuilder
        """
        clone = FilterBuilder()
        clone.raw_inline = self.raw_inline
        return clone
    
    def _add_to_raw(self, operator: str, raw: str) -> "FilterBuilder":
        """Adds to the filter raw and joins with the operator. MUTATES THE OBJECT

        Args:
            operator (str): The operator to join with
            raw (str): The raw to add to the filter

        Returns:
            FilterBuilder: self
        """
        if len(self.raw_inline) <= 0:
            self.raw_inline += raw
        elif self.raw_inline.endswith("("):
            self.raw_inline += raw
        else:
            self.raw_inline += f' {operator} {raw}'
        return self

    def __str__(self) -> str:
        return f"(r) => {self.raw_inline}"