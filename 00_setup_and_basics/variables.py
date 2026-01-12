"""
variables.py

Intro to Python variables and basic usage.

Time Complexity: O(1) for all demonstrations.
Space Complexity: O(1).
"""


def demo_variables() -> None:
    """Demonstrate variable declaration and basic printing."""
    # Integer
    age: int = 20

    # Float
    height: float = 5.9

    # String
    name: str = "Alice"

    # Boolean
    is_student: bool = True

    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


def variable_reassignment() -> None:
    """Demonstrate variable reassignment and type flexibility."""
    x = 10
    print(f"x starts as: {x} (type: {type(x).__name__})")
    
    x = "Hello"
    print(f"x reassigned to: {x} (type: {type(x).__name__})")
    
    x = 3.14
    print(f"x reassigned to: {x} (type: {type(x).__name__})")


def multiple_assignment() -> None:
    """Demonstrate multiple variable assignment."""
    # Assign same value to multiple variables
    a = b = c = 100
    print(f"a={a}, b={b}, c={c}")
    
    # Assign different values in one line
    x, y, z = 1, 2, 3
    print(f"x={x}, y={y}, z={z}")
    
    # Swapping variables
    x, y = y, x
    print(f"After swap: x={x}, y={y}")


if __name__ == "__main__":
    print("=== Demo Variables ===")
    demo_variables()
    
    print("\n=== Variable Reassignment ===")
    variable_reassignment()
    
    print("\n=== Multiple Assignment ===")
    multiple_assignment()
