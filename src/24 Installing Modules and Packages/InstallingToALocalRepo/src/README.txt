This is an example Python module (mypackage).
Use the scripts as follows:

1) build.py     - this will create a source distro and then move it to our web server
2) server.py    - start web server on localhost at port 8000
3) install.py   - use pip to download and install from local repo
                - server must be running
4) unistall.py  - uninstall package using pip
5) test.py      - verify it worked

N.B. By default, setup.py sdist does not place non Python source files in 
generated tarballs, so specify them in MANIFEST.IN
