
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
