#!/bin/sh
apt-get update
apt-get install gmsh -y
apt install python-numpy

tar xzvf murtazo.tgz
cd murtazo
tar xvf cloudnaca.tgz
tar xvf navier_stokes_solver.tar

cd navier_stokes_solver/src
./compile_forms
cd ..
cmake .
make -j 2

cd ../cloudnaca
sed -i 's|/Applications/Gmsh.app/Contents/MacOS/gmsh|/usr/bin/gmsh|g' runme.sh
./runme.sh 0 30 10 200 3

cd ..
cd ..
python3 convert.py
