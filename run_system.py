import subprocess
import os

subprocess.call('rm check.csv', shell=True)

subprocess.call("python make_csv.py", shell=True)

subprocess.call("mv check.csv system/final.csv", shell=True)
subprocess.call("cd system && make", shell=True)
