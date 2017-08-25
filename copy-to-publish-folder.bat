:start
cls
@echo off
echo.
echo.
echo Copy files to the publish location and open the publisher
echo Only currently works for standalone files and does only
echo work on shots (with sequence associated)
echo.
echo.
set /P seq=Sequence:   
echo.
echo.
set /P shot=Shot:   
echo.
echo.
echo Where did the file come from?
echo.
echo 1. ingest (from a vendor)
echo 2. output (produced inhouse)
echo.
set /P to=: 
if /I "%to%" EQU "1" set to=ingest
if /I "%to%" EQU "2" set to=output
:echo %to%
echo.
echo.
echo What is the file type?
echo.
echo 1. camera
echo 2. cuts
echo 3. elements
echo 4. geo
echo 5. mattes
echo 6. plates
echo 7. ref
echo 8. textures
echo.
set /P type=Type: 
if /I "%type%" EQU "1" set type=cam
if /I "%type%" EQU "2" set type=cuts
if /I "%type%" EQU "3" set type=elements
if /I "%type%" EQU "4" set type=geo
if /I "%type%" EQU "5" set type=mattes
if /I "%type%" EQU "6" set type=plates
if /I "%type%" EQU "7" set type=ref
if /I "%type%" EQU "8" set type=textures
echo.
echo.
set /P fp=Drag and drop the folder/filepath:  
echo.
echo.
set nfp=\\192.168.50.10\FilmShare\dng02_mae\sequences\%seq%\%seq%_%shot%\_publish\%to%\%type%
echo Preparing to copy %fp%
echo to
echo %nfp%

echo Copying...
mkdir "%nfp%"
copy /Y /V "%fp%" "%nfp%" 

start "" \\192.168.50.10\FilmShare\dng02_mae\_shotgun\tank.bat publish
start "" explorer.exe %nfp%


pause
goto start