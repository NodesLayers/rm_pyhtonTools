import os
import glob

for f in os.listdir('y:/'):
    print(f)
#print(os.listdir('y:/'))
print()
print()

job = input("Job to load into environement: ")
print ("Jobbing into ",job)