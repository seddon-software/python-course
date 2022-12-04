import os
# os.chdir("tutorials")
# os.system("which python")
import tkinter as tk

import matplotlib.pylab as plt
plt.ion()
#matplotlib.use('TkAgg')
from bluesky import RunEngine
import ophyd
ophyd.__version__ = "1.7.1"
RE = RunEngine({})
from bluesky.callbacks.best_effort import BestEffortCallback
bec = BestEffortCallback()

# Send all metadata/data captured to the BestEffortCallback.
RE.subscribe(bec)

# Make plots update live while scans run.
from bluesky.utils import install_kicker
#matplotlib.use('TkAgg')
#install_kicker()

from bluesky.plans import count
from ophyd.sim import det1, det2  # two simulated detectors
dets = [det1, det2]   # a list of any number of detectors

RE(count(dets))
from databroker import Broker
db = Broker.named('temp')

# Insert all metadata/data captured into db.
RE.subscribe(db.insert)

from bluesky.utils import ProgressBarManager
RE.waiting_hook = ProgressBarManager()

from ophyd.sim import det, motor
from bluesky.plans import scan
dets = [det]   # just one in this case, but it could be more than one

X = RE(scan(dets, motor, -1, 1, 10))
import BlueskyEventStream
BlueskyEventStream.read()
