
##### Standard flows ######
""" in CLI:
-Standard input
-Standard outpout
-Standard error

>>> import sys
>>> sys.stdin # standard input
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
>>> sys.stdout # standard output
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
>>> sys.stderr # standard error
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
>>>

It's very similar to files flow with encoding, mode etc.
in --> read
error & out --> write

>>> sys.stdout.write("a test.")
a test.7 (7 is the length)
Now, add \n

>>> sys.stdout.write("a test.\n")
a test.
8

###  How to modify standard flows ? ###
>>> my_file = open('output.txt', 'w') # create open file object
>>> my_file
<_io.TextIOWrapper name='output.txt' mode='w' encoding='UTF-8'>
>>> sys.stdout = my_file  # Redirect this object into standart output flow.
>>> print("Something to write…") # Return nothing on the screen, The screen is not standard ouput anymore.
>>> quit()
erfaliel@SurfaceVincent:~$ ls -rtl
total 0
lrwxrwxrwx 1 erfaliel erfaliel 34 Jul  7  2018 dev -> /mnt/c/Users/Vincent/Documents/dev
-rw-rw-rw- 1 erfaliel erfaliel 86 May 27 17:05 output.txt   !!! standard output is a file now!!!
erfaliel@SurfaceVincent:~$ cat output.txt

### origin object is here : 
>>> sys.__stdout__
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
>>> sys.__stdin__
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
>>> sys.__stderr__
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
>>>

"""
#### Signals ######
""" in CLI:
SIGINT : to send end program signal. (termination)

>>> import signal
>>> signal.SIGINT
<Signals.SIGINT: 2>
>>>
### How to interecpt this signal ?###
>>> import sys
>>> def close_program(signal, frame):
...     \""" Function called when it's time to close our application.\"""
...     print("It's time !")
...     sys.exit(0)
...
exit is a function from sys module that stop a program an return a code where 0 is normal ternination.
Now we have to connect SIGINT to our function
--> signal([signal to intercept], [reference to the function to execute])
(reference to the function means the name of the function without double paranthesis)

Now we are going to check with a loop and an interuption from the user:

>>> print("This program is a loop… Please interrupt me!")
This program is a loop… Please interrupt me!
>>> while True:
...     continue
...
^CIt's time !
«It's time» message means connection between the SIGINT and our function is effective

"""
#### Arguments interpreter ###
""" look at the file consol_test.property
and execute:
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 consol_test.py
['consol_test.py']

erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 consol_test.py arguments
['consol_test.py', 'arguments']

erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 consol_test.py argument1 argument2 argument3
['consol_test.py', 'argument1', 'argument2', 'argument3']

So first agrument of sysargv is the program name and if they exits you can have the rest of the list
"""
### How to interpret those arguments ?
### Simple action exemple
"""
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 simple_argv_exemple.py stop
Shuting down
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 simple_argv_exemple.py start
Starting up
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 simple_argv_exemple.py restart
Stop and Start…
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 simple_argv_exemple.py status
the status is : XXX
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 simple_argv_exemple.py check
command check is uknown !
"""

#### More complex
"""
by default the -h --help options are known by default in linux:
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 argparse_example.py -h
usage: argparse_example.py [-h]

optional arguments:
  -h, --help  show this help message and exit

by convention -[one letter] (short option version) = --[ome word] (long option version)
TO add argument in the parser:
parser.add_argument("x", help="number tu put in square") # To add argument
if you run :
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 argparse_example.py -h
usage: argparse_example.py [-h] x

positional arguments:
  x           number tu put in square

optional arguments:
  -h, --help  show this help message and exit

  --> We have just add one parameter with option help that add the help menu.help

-So if we add this
args = parser.parse_args() # method to return arguments pass to the program.

print("you have specified x =", args.x) # Print the x argument 
we can get :
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 argparse_example.py 5
you have specified x = 5

-We can be more specific :
import argparse
parser = argparse.ArgumentParser() # argument parser object created
parser.add_argument("x", type=int, help="number tu put in square") # To add argument
args = parser.parse_args() # method to return arguments pass to the program.

x = args.x
result = x ** 2
print("square =", result)

Result:
----------
erfaliel@SurfaceVincent:~/dev/comparaison_de_codes/10-Specific_Dev/3-os_sys$ python3 argparse_example.py 5
square = 25

python3 argparse_example.py test
usage: argparse_example.py [-h] x
argparse_example.py: error: argument x: invalid int value: 'test'
"""
#### All tuto in https://docs.python.org/3/howto/argparse.html
""" Exemple : argparse_verbosity.py to look for about count option
_Dev/3-os_sys# python3 argparse_verbosity.py -h
usage: argparse_verbosity.py [-h] [-v] square

positional arguments:
  square         display the square of e given number

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase input versbosity

#argparse_verbosity.py 5
25
# python3 argparse_verbosity.py -v 5
5^2 == 25
# python3 argparse_verbosity.py -vv 5
The square of 5 equals 25
#

