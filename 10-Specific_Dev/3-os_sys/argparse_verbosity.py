import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, 
                    help="display the square of e given number")
parser.add_argument("-v", "--verbose", action="count",
                    help="increase input versbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
    print("The square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
