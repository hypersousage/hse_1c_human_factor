#!/bin/bash

cp vtype_gen.py ../
cp osmWebWizard.py ../
cp -r webWizard ../
cp randomTrips.py ../

cd ..

default_port=8080

if [[ $1 == 2 ]]
then
    number=$RANDOM%10
    default_port=8080
    port=$(($default_port+$number+1))
    echo port1 $default_port
    echo port2 $port
    python3 osmWebWizard.py | python3 osmWebWizard.py --port $port
else
    echo port $default_port
    python3 osmWebWizard.py
fi