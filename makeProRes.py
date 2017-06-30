import os
import sys
import subprocess

# Path to FFmpeg
ffmpeg = os.path.normpath("C:\\Users\\studio\\Downloads\\ffmpeg-20170628-c1d1274-win64-static\\ffmpeg-20170628-c1d1274-win64-static\\bin\\ffmpeg.exe")

try:
    filePath = sys.argv[1]
    filePath = os.path.normpath(filePath)
except:
    filePath = input("Input filepath to convert: ")

# Find all files in folder
for f in os.walk(filePath, topdown=True):
    fileList = str(f[-1])
    fileList = fileList.replace("[","")
    fileList = fileList.replace("]","")
    fileList = fileList.replace("'","")
    fileList = fileList.replace(" ","")
    fileList = fileList.split(",")

# first file
f = fileList[0]
if f.split(".")[-1] == "mov":
    f = fileList[1]
print ("First Filename: "+f)

# Extension
ext = f.split(".")[-1]
print("Input Extension: "+ext)


# Assumed Framenumber of first file
fn = f.replace("_", ".")
fn = fn.split(".")
fn = fn[-2]
print ("Framenumber of first file: "+fn)

# Hashes to replace
fnl = len(fn)
if fnl == 1:
    fnl = "%01d"
if fnl == 2:
    fnl = "%02d"
if fnl == 3:
    fnl = "%03d"
if fnl == 4:
    fnl = "%04d"
if fnl == 5:
    fnl = "%05d"        
if fnl == 6:
    fnl = "%06d"
    
# Replace framenumber with hashes
f = f.replace(fn, fnl)
print(f)


firstFilePath = os.path.join(filePath, f)
#firstFilePath = firstFilePath.replace(fn, "*")
print(firstFilePath)



# Output Filename
outputFile = f.replace(str(fnl), "")
outputFile = outputFile.replace("."+ext, "")
outputFile = os.path.join(filePath, outputFile+".mov")
outputFile = outputFile.replace("..", ".")
print("Output Filepath: "+outputFile)





# Create CMD call
cmd = ffmpeg+" -y -start_number "+fn+" -i "+firstFilePath+" -framerate 24 -vcodec prores_ks -pix_fmt yuva444p10le -profile:v 4444 -bits_per_mb 8000 "+outputFile
#cmd = cmd = ffmpeg+" -y -f mov -i "+firstFilePath+" f "+outputFile


# Invoke FFMPEG
subprocess.Popen(cmd)

    
    
    
#print(mode)
  
#if mode == cmd:
 #   file to conc


#ffmpeg -y -f mov -i input-file.mov -vcodec prores_ks -pix_fmt yuva444p10le -profile:v 4444 -bits_per_mb 8000 -s 1920x1080 output-file.mov