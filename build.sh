#!/bin/sh
PYTHON=python3.12
PYTHONLIBVER=python$(python3.12 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3.12-config --abiflags)
BASEDIR=$(dirname $0)
DAY=$1

mkdir -p ${BASEDIR}/dist


cython -3 ${BASEDIR}/src/day${DAY}.py --embed

gcc -Os $(python3.12-config --includes) src/day${DAY}.c $(python3.12-config --ldflags) -l$PYTHONLIBVER -o dist/day${DAY} 
