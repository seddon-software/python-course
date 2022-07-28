#! /bin/bash

mkdir -p $(jupyter --config-dir)/custom
printf 'Do you want to add custom styles to the notebook (y/n): ' 
read reply
if [ $reply == "y" ]
then
    cp ./config/jupyter_notebook_config.py $(jupyter --config-dir)
fi

printf 'Do you want to add a simple configuration file to the notebook (y/n): '
read reply
if [ $reply == "y" ]
then
    cp ./config/custom.css $(jupyter --config-dir)/custom
fi

