#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> 21df5dbd623a82de9567361e198ae9da9459b0c2
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print(args, "arguments.")
    elif args == 1:
        print(args, "argument:")
        print("{}: {}".format(args, sys.argv[1]))
    else:
<<<<<<< HEAD
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
=======
        print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
>>>>>>> 21df5dbd623a82de9567361e198ae9da9459b0c2
