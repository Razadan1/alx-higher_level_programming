def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if value is int:
            return True
        else:
            return False
    except ValueError:
        pass
