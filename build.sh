#!/bin/sh
DAY=$1
mkdir -p dist
python -m nuitka src/day${DAY}.py --standalone --output-dir=dist
