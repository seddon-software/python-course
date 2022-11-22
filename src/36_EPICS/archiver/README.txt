The following notes were provided by Andy Wilson:

The current in the storage ring is SR-DI-DCCT-01:SIGNAL. 
The normal value is around 300 mA during run time and around 0 mA when the beam is off. 
If you plot it over a couple of months, you can see the differences between run and shutdown. 
When you focus on a week, you can see any beam-loss events, and machine development days. 
If you look at a couple of hours of run, you can see steps up every 10 minutes, when the Topup system 
injects some more electrons, and the following exponential decay as they are gradually lost.

The lifetime in hours of the decay of the stored beam is CS-CS-MSTAT-01:LIFETIME. 
A countdown in seconds to the start of the next topup cycle is SR-CS-FILL-01:STACOUNTDN. 
If you look at all of these together it can be somewhat interesting.

If you want values which are always changing but stay near a certain value, you can look at the pressure readings 
from vacuum gauges. 
For example, BL08I-VA-GAUGE-02:P is the second vacuum gauge on beamline I08. You can change the 08 for another number 
between 02 and 24, and the I for a B, to see some different beamlines (not all combinations exist).
