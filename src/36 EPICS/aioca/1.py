import os
os.environ['EPICS_CA_MAX_ARRAY_BYTES'] = '1000000'

import asyncio
from aioca import caget, caput, camonitor, run

async def do_stuff():
    # Using caput: write 1234 into PV1.  Raises exception on failure
    pv = 'chris:amplitude'
    await caput(pv, 1.0)

    # Print out the value reported by PV2.
    print(await caget(pv))

    # Monitor PV3, printing out each update as it is received.
    def callback(value):
        print('callback', value)

    camonitor(pv, callback)

# Now run the camonitor process until interrupted by Ctrl-C.

# the code below is equivalent to this line
# run(do_stuff(), forever=True)

loop = asyncio.get_event_loop()
loop.create_task(do_stuff())
loop.run_forever()
