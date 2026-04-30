'''
Nexus
=====

A scientific data standard, not just a file format
Designed for neutron, X-ray, and synchrotron experiments
Built on top of HDF5
has rules on how to organize folders and labels

Each section has a defined meaning:
    entry → root of experiment
    instrument → equipment details
    sample → what was measured
    data → measured results

At Diamond Nexus files are produced on the beamlines.  The beamlines have software to analyse these files (for example Dawn), but
also can be analysed in Python using HDF5 software.
'''

import webbrowser as wb
wb.open("http://web.mit.edu/fwtools_v3.1.0/www/H5.intro.html")

