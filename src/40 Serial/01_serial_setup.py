import os, serial

def setupTerminalEmulators():
    cmd = "socat -d -d pty,raw,echo=0 pty,raw,echo=0"
    os.system(f"{cmd} &")

setupTerminalEmulators()

