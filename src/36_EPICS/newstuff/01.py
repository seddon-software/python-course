import matplotlib
from bluesky import RunEngine

RE = RunEngine({})

from bluesky.callbacks.best_effort import BestEffortCallback
bec = BestEffortCallback()

# Send all metadata/data captured to the BestEffortCallback.
RE.subscribe(bec)

# Make plots update live while scans run.
matplotlib.use("Qt5Agg", force=True)
# 

from databroker import Broker
db = Broker.named('temp')

# Insert all metadata/data captured into db.
RE.subscribe(db.insert)

from bluesky.utils import ProgressBarManager
RE.waiting_hook = ProgressBarManager()

from ophyd.sim import det1, det2  # two simulated detectors

from bluesky.plans import count
dets = [det1, det2]   # a list of any number of detectors

print(RE(count(dets)))

# five consecutive readings
print(RE(count(dets, num=5)))

# five sequential readings separated by a 1-second delay
print(RE(count(dets, num=5, delay=1)))

# a variable delay
print(RE(count(dets, num=5, delay=[1, 2, 3, 4])))
