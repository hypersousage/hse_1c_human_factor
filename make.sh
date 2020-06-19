#!/bin/bash

cp vtype_gen.py ../
cp osmWebWizard.py ../
cp -r webWizard ../
cp randomTrips.py ../

cd ..
number=$RANDOM%10
default_port=8080
port=$(($default_port+$number))
echo port $port
python3 osmWebWizard.py --port $port