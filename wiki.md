## jailw1n wiki.

Welcome, to jailw1n wiki! This wiki helps you to make your jailbreak process more stable.

## Requirements.

- checkm8 device (A8(X)-A11).
  - On A11 devices, you must disable password while you in jailbroken state, and if you on iOS 16, backup your device via iTunes and restore it via settings app and **don't set password again**!
- iTunes 12.6.5 installed on your pc.
- Intel processor.
  - AMD processor have an issue [with (likely) their USB controllers] that causes them to have a very low success rate with checkm8. But you need to try, maybe you'll be lucky :).
- Zadig driver tool.
- MSYS2.

# Jailbreak steps.
## Step 1. Prepairing.

Lets start with basic.

1. Install or downgrade iTunes to version 12.6.5.
2. Install Zadig driver tool.
3. Put your iDevice in DFU mode.
4. Download jailw1n from GitHub.

### Errors.

- If iTunes says, that iTunes Library.itl from newer version, go to C:\Users\~your username~\Music\iTunes\iTunes Library.itl and delete it. Rerun iTunes and it must open.
- If your iDevice cannot go to DFU mode, check the cable, it must be plugged to PC.

## Step 2. Switiching driver.

1. While you iDevice in DFU mode, open Zadig.
2. In Zadig open "Apple Mobile Device (DFU Mode)".
3. Replace WinUSB driver to libusbK, and press "Replace Driver" button.
4. Wait until Zadig switch drivers.

### Errors.

- If there is no "Apple Mobile Device (DFU Mode)" in Zadig menu, unplug and replug device, it shoud appear.

## Step 3. Running jailbreak.

1. Open jailw1n app.
2. Press start buttom.
3. Wait until it will complete.
4. When your device will boot, open "palera1n" app, and install package manager.

### Errors.

- If script ends on iTunes error. You didn't install iTunes or install to another disk, replace it to disk C:\.
- If app ends on MSYS2 error. You didn't install MSYS2 or install to another disk, replace it to disk C:\.
- If there is error with jailbreak, go to Discord server(not availible now), and open an Issue in channel "Issues", and i will try to help you. (Don't forget about log.)

# Installing meowbrek.
## If you don't want rejail via PC, use meowbrek.
## This will work if you on iOS 15.0-15.7.6!

1. Install jailw1n and stay on QR-Code page.
2. Bootstrap you device.
3. Install "TrollHelper" and "TrollStore".
4. Scan QR-Code in camera, and download meowbrek.
5. Install meowbrek via TrollStore.
6. Reboot your iDevice.
7. Open meowbrek and wait one minute until press "Jailbreak".
8. Press "Jailbreak" and wait.

# Removing jailbreak.

1. Go to "palera1n" app.
2. Press "Revert Install".
3. Reboot device.
## If you using meowbrek, use this steps. (TrollStore will be still installed.)
1. Reboot device.
2. Run jailbreak via "jailw1n".
3. Open "palera1n" app.
4. Press "Revert Install".
5. Reboot device.
