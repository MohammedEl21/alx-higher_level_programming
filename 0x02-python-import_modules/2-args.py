<<<<<<< HEAD
=======
#!/usr/bin/python3

>>>>>>> adc4c155194189012797298b7d2b057c12600bad
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
<<<<<<< HEAD

=======
>>>>>>> adc4c155194189012797298b7d2b057c12600bad
