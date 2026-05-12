@echo off
 echo 800 x 600 @ 240 
 nircmd.exe setdisplay 800 600 32 240
 timeout /t 2 /nobreak >nul 
 echo Launching CS2 
 start steam://rungameid/730//-windowed -noborder -w 800 -h 600 -freq 240