import time
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any: # Can parse any function, no matter the number of arguments
        start_time: float = time.time() # Start time
        result: Any = func(*args, **kwargs) # Call the decorated function
        end_time: float = time.time() # end time
        print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec.")
        return result
    
    return wrapper

@timer # Replacement of : example_function = timer(example_function)
def example_function(n: int) -> str:
    return f"The sum is {sum(range(n))}"

print(example_function(1_000_000))
