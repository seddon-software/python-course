'''
aioca has an almost identical API to cothread and catools
additionally it allows you to work with other asyncio libraries
'''

import os
os.environ['EPICS_CA_MAX_ARRAY_BYTES'] = '1000000'

import asyncio
from aioca import caget, caput, camonitor, run

async def do_stuff():
    # Using caput: write into pv.  Raises exception on failure
    pv = 'chris:amplitude'
    await caput(pv, 1.0)

    # Print out the value reported by pv.
    print(f"{pv} = {await caget(pv)}")

    # Monitor pv, printing out each update as it is received.
    def callback(value):
        print(f'callback: {pv} = {value}')

    camonitor(pv, callback)
    await caput(pv, 2.0)
    await caput(pv, 3.0)
    await caput(pv, 4.0)

# Now run the camonitor process until interrupted by Ctrl-C.

# the code below is equivalent to this line
# run(do_stuff(), forever=True)

loop = asyncio.get_event_loop()
loop.create_task(do_stuff())
loop.run_forever()
