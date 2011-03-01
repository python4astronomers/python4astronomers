#!/bin/sh

#./clean.sh

#export CFLAGS="-mtune=core2 -finline-functions"
#export LD_LIBRARY_PATH="/data/scialg/staff/brefsdal/linux64/lib"
#export PATH="/data/scialg/staff/brefsdal/linux64/bin:${PATH}"

python setup.py build_ext --inplace
