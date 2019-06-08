import sys

if len(sys.argv) < 2:
    print("We need a parametter as action")
    sys.exit(1)

task = sys.argv[1]

if task == "start":
    print("Starting up")
elif task == "stop":
    print("Shuting down")
elif task == "restart":
    print("Stop and Start…")
elif task == "status":
    print("the status is : XXX")
else:
    print("command {} is uknown !".format(task))