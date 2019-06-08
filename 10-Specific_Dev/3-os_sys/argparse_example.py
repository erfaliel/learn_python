import argparse
parser = argparse.ArgumentParser() # argument parser object created
parser.add_argument("x", type=int, help="number tu put in square") # To add argument
args = parser.parse_args() # method to return arguments pass to the program.

x = args.x
result = x ** 2
print("square =", result)