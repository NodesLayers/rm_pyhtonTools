import os
import sys
import shutil
import subprocess

    

fp = sys.argv[1]    
fp = os.path.normpath(fp)
fp = fp.replace("/", os.sep)
fp = fp.replace("\\", os.sep)


end = ""

while end != "export":
    bn = os.path.basename(fp)
    fp = os.path.split(fp)[0]
    end = os.path.split(fp)[1]

#        print ""
#        print bn
#        print fp
#        print end
else:
    #print ""
    #print "MATCH"
    print ("")
    print ("Deleting the following folder: ")
    print (os.path.join(fp, bn))

    removePath = os.path.join(fp, bn)
    try:
        shutil.rmtree(removePath)
    except:
        print ("Failed to delete "+removePath)
