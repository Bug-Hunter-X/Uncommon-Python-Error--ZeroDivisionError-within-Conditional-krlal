def function_with_uncommon_error(x):
    if x == 0:
        return "Division by zero is not allowed" # Handle ZeroDivisionError gracefully
    else:
        return x + 1

result = function_with_uncommon_error(0)  # This will now print a message instead of crashing
print(result) # Output: Division by zero is not allowed