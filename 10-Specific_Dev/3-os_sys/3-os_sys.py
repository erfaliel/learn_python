
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
"""
##### System ########################################################
""" os.system prints the result of a command and return the status code.
you can capture the status code, not the result. Python makes return even if
the command is still in progress. (sleep 5 don't stop python for 5 seconds).

import os
os.system("ls")

"""
#os.popen
"""
command in parameter, but it returns au object with "pipe" we allowe you to read the command return.

import os
>>> os.system("sleep 5")
0
>>> cmd = os.popen("ls")
>>> cmd
<os._wrap_close object at 0x7fa40631f908>
>>> cmd.read()
'10-Specific_Dev\n1-conditions\n2-Iterations_et_Comprehensions__Basic__\n3-fonctions\n4-exceptions\n5-Objets-vs-Types-andFiles\n6-Variables-reference-affectation-vs-PatternMatching\n7-Objets\n8-Iterators_and_Generators__Advanced__\n9-Advanced_Concept_Classes\ngeometry.py\nobject_file\nREADME.md\n'

But pipe is blocked the program untill the command is ending.
"""
#subprocess module (from http://queirozf.com/entries/python-3-subprocess-examples)
"""
the simplest way when you don't need parameters:
>>> import subprocess
>>> subprocess.call("ls")
dev  output.txt
0

#parameters needs to be passed with a list:
>>> from subprocess import run, Popen
>>> run(["ls", "-rtl", "."])
total 0
lrwxrwxrwx 1 erfaliel erfaliel 34 Jul  7  2018 dev -> /mnt/c/Users/Vincent/Documents/dev
-rw-rw-rw- 1 erfaliel erfaliel 86 May 27 17:05 output.txt
CompletedProcess(args=['ls', '-rtl', '.'], returncode=0) # we get a returncode !

# Raise an exception if the underlaying process errors.
>>> run("./MyScriptDoesNotExist")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/subprocess.py", line 403, in run
    with Popen(*popenargs, **kwargs) as process:
  File "/usr/lib/python3.6/subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.6/subprocess.py", line 1344, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: './MyScriptDoesNotExist': './MyScriptDoesNotExist'

# The same with shell=True option
>>> run("./MyScriptDoesNotExist", shell=True)
/bin/sh: 1: ./MyScriptDoesNotExist: not found
CompletedProcess(args='./MyScriptDoesNotExist', returncode=127)

# The Same with shell=True and check=True (enforce exception)
>>> run("./MyScriptDoesNotExist", shell=True)
/bin/sh: 1: ./MyScriptDoesNotExist: not found
CompletedProcess(args='./MyScriptDoesNotExist', returncode=127)
>>> run("./MyScriptDoesNotExist", shell=True, check=True)
/bin/sh: 1: ./MyScriptDoesNotExist: not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.6/subprocess.py", line 418, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command './MyScriptDoesNotExist' returned non-zero exit status 127.


# How to capture stdout and stderr in a file (log file):
python3 output_in_files.py
see out.txt
see err.txt

Here the code and explanation.



follow http://queirozf.com/entries/python-3-subprocess-examples


#how to capture the return: the subrocess.popen combo.
>>> my_out = subprocess.Popen(["ls", "-rtl", "."], \
...             stdout=subprocess.PIPE, \
...             stderr=subprocess.STDOUT)
>>> (stdout, stderr) = my_out.communicate()
>>> print(stderr)
None
>>> print(stdout)
b'total 0\nlrwxrwxrwx 1 erfaliel erfaliel 34 Jul  7  2018 dev -> /mnt/c/Users/Vincent/Documents/dev\n-rw-rw-rw- 1 erfaliel erfaliel 86 May 27 17:05 output.txt\n'







