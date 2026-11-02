"""A small package for greeting people from the command line."""

import sys


def greet(name: str) -> str:
    """Return a greeting for the given name.

    :param name: The name to greet.
    :returns: A greeting that includes the given name.
    """
    return f"Hello, {name}!"


def main() -> int:
    """Print a greeting for the first command-line argument, or ``world``."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0
