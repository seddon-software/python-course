# Install pylint
#   sudo apt-get install pylint

# create a configuration file for pylint
#   pylint --generate-rcfile > .pylintrc

# note:
#  I've changed to camelCase and allowed variables:  x, y, z and dx, dy, dz

import os

# run the test
os.system("pylint classAttributes.py")
