import keyword

def is_keyword(name: str) -> bool:
    return name in keyword.kwlist
