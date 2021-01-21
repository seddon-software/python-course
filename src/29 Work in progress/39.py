import os, gdb

path = "/home/chris/home/workspace/cpp/04_STL"
os.chdir(path)

os.system("ls")


import os
import sys
LOG_FILE='/tmp/gdb.log'
# attach GDB to list of files
this_file = [
            'file1.c',
            'file2.c',
            ]
this_fn = [
            'fn1',
            'fn2',
          ]
def setup():
    print('Running GDB from: %s\n'%(gdb.PYTHONDIR))
    gdb.execute("set pagination off")
    gdb.execute("set print pretty")
    # if connecting to remote target
    # gdb.execute('target remote <ip>:<port>')
    gdb.execute('set logging file %s'%(LOG_FILE))
    gdb.execute('set logging on')
    print('\nReading gdb env..\n')
    gdb.execute('show script-extension')
    gdb.execute('show sysroot')
    gdb.execute('show solib-search-path')
    print('\nSetup complete !!\n')
# what to do when a breakpoint is hit
def stop_handler(event):
    print('EVENT: %s' % (event))
    gdb.execute("info local")
    gdb.execute("info threads")
    gdb.execute("info args")
    gdb.execute("bt")
    if event.breakpoint.location == "func3":
        gdb.write("Special bp hit\n")
        gdb.execute("p func3_var")
        gdb.execute("p *func3_ptr")
    # don't stop, continue
    gdb.execute("c")
# set bp on all the functions specified in all the files specified in 'this_file'
def set_bp_from_files():
    for f in this_files:
        try:
            gdb.execute("rbreak %s:."%(f))
            print('rbreak %s:.'%(f))
        except:
            print('Error inserting breakpoint %s'%(fn))
    print('\nDone setting breakpoints from list of files\n')
# set breakpoint on all the functions specified in 'this_fn'
def set_bp_from_funs():
    for fn in this_fn:
        if fn:
            try:
                gdb.Breakpoint(fn)
                print('break ' + fn)
            except:
                print('Error inserting breakpoint %s'%(fn))
    print('\nDone setting breakpoints from list of funs\n')
def register_stop_handler():
    gdb.events.stop.connect(stop_handler)
    #unregister
    #gdb.events.stop.disconnect(stop_handler)
    print('\nDone setting stop-handler\n')
def main():
    setup()
    set_bp_from_funs()
    set_bp_from_files()
    register_stop_handler()
    #gdb.execute("c")
main()