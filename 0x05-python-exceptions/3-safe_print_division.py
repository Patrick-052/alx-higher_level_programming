#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
        print("Can't divide by zero")
    finally:
        print("Inside result: {}".format(result))
    return result
