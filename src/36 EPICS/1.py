pipenv install cothread
pipenv run python
then:
    import cothread
    from cothread.catools import *
    caget("chris:amplitude")
    caput("chris:amplitude", 0.5)


Now start the IOC running with:
./bin/linux-x86_64/stexercise1.boot
Open another terminal
cd  $HOME/chris/ioc
Now start the GUI running with:
./data/startgui1