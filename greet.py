def greet(name: str, formal: bool = False) -> str:
    """Greet a person by name."""
    if formal:
        return f"Good day, {name}."
    return f"Hello, {name}!"
