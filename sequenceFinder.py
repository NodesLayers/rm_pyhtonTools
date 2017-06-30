import os
import sys

for f in os.walk("Y:\dng02_mae\client_io\in\SORTING\SEQUENCES\BSA\BSA_0450\Elements\E_bsa_0450_blind_energyBall_rgba", topdown=True):
    fileList = str(f[-1])
    fileList = fileList.replace("[","")
    fileList = fileList.replace("]","")
    fileList = fileList.replace("'","")
    fileList = fileList.replace(" ","")
    fileList = fileList.split(",")
    
    print (fileList[0], fileList[-1])