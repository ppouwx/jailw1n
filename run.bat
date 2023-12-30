@echo off
echo jailw1n started!
echo checking bin's and files...

if not exist "C:\Program Files\iTunes\iTunes.exe" (
    if not exist "C:\Program Files (x86)\iTunes\iTunes.exe" (
        echo Oh no! There is no iTunes!.
        echo Please install iTunes 12.6.5 or older before proceeding.
        exit
    )
)

if not exist "C:\jailw1n\bin" (
    if not exist "C:\jailw1n\bin\nokpf4u.bin" (
        echo Oh no! Seem's you removed KPF file!
        echo Please disable Windows Defender and reinstall jailw1n.
        exit
    )
)

if not exist "C:\jailw1n\bin" (
    if not exist "C:\jailw1n\bin\nooverlay4u.bin" (
        echo Oh no! Seem's you removed Overlay file!
        echo Please disable Windows Defender and reinstall jailw1n.
        exit
    )
)

if not exist "C:\jailw1n\bin" (
    if not exist "C:\jailw1n\bin\noramdisk4u.bin" (
        echo Oh no! Seem's you removed Ramdisk file!
        echo Please disable Windows Defender and reinstall jailw1n.
        exit
    )
)

if not exist "C:\jailw1n\bin" (
    if not exist "C:\jailw1n\bin\pongoOS_shellcode.bin" (
        echo Oh no! Seem's you removed PongoOS Shellcode file!
        echo Please disable Windows Defender and reinstall jailw1n.
        exit
    )
)

echo Everything here! Now let's run openra1n code!

C:\msys64\mingw64.exe "./postrun.sh"