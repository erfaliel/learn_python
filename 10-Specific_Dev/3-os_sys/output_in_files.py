import subprocess
import sys

#Create two files to hold the output
with open('out.txt', 'w+') as fout:
    with open('err.txt', 'w+') as ferr:
        out = subprocess.run(["ls", "-lha"], stdout=fout, stderr=ferr)
        # reset file tou read from it
        fout.seek(0)
        # save output (if any) in variable
        output = fout.read()

        #reset file tou read from it
        ferr.seek(0)
        # save errours (if any) invariale
        errors = ferr.read()
#output
#errors
