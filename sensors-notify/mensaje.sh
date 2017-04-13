#!/bin/bash

export DISPLAY=:0

# get_temp es un script en python que parsea la salida
# del comando 'sensors'
temp=$(/home/kaoz/.stuff/sensors-notify/get_temp.py);
if [ $temp -gt 70 ]
then
    i3-nagbar -t warning -m "La temperatura sobrepasa los 70ºC ($temp)";
elif [ $temp -gt 90 ]
then
    i3-nagbar -t error -m "La temperatura sobrepasa los 90ºC ($temp)";
fi
