@echo off

echo #############################################################
echo #--------------------------bakew1n--------------------------#
echo #-----------------------------------------------------------#
echo #------Script made by ppouwx. openra1n made by mineek.------#
echo #-----------------bakera1n made by dora2iOS.----------------#
echo #-----------------------------------------------------------#
echo #------------Proudly written on Windows Notepad.------------#
echo #-----------------------------------------------------------#
echo #############################################################
echo .
echo Before we start...
echo . 
echo This tool only for developers. Remember, it just proof-of-concept that jailbreak can succsesfully run on WindowsOS, without any LiveUSB and Linux virtual machines.
echo I'm not responsible for bricking device, data loss, broken alarms and etc. If you downloading this program, YOU accepting all the risk, and YOU taking all the responsibilty for probable harming device.
echo If you accept all of this warnings, just press any button, and prepare you iDevice.

pause >nul

if not exist "C:\Program Files\iTunes\iTunes.exe" (
    if not exist "C:\Program Files (x86)\iTunes\iTunes.exe" (
        echo Whoops. I didn't see any iTunes program.
        echo To continue, install iTunes 12.6.5 or older.
        echo If you have iTunes, maybe it on another disk. Move it to C:\.
        echo Re-run script when you're ready.
        echo If you have some problems open Issue on github.
        echo Also, read an install.md on GitHub.
        pause >nul
        exit
    )
)

if not exist "C:\msys64\msys2.exe" (
    echo Whoops. I didn't see any MSYS2 program.
    echo To continue, install MSYS2.
    echo If you have MSYS2, maybe it on another disk. Move it to C:\.
    echo Re-run script when you're ready.
    echo If you have some problems open Issue on github.
    echo Also, read an install.md on GitHub.
    pause >nul
    exit
)

C:\msys64\msys2.exe "./restore.sh"

rem Add the argument at the end of the line above if needed
rem Examples:
rem C:\msys64\msys2.exe "./restore.sh" --no-device
rem C:\msys64\msys2.exe "./restore.sh" --entry-device --no-color
