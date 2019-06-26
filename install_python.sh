#!/bin/bash

REQUIRED="3.7.0"
DETECTORPATH=$PWD
VERSION=$(python -c \
"print('$REQUIRED'.rpartition('.')[0] \
if '$REQUIRED'.count('.') >= 2 \
else '$REQUIRED')")

cd $DETECTORPATH
make clean
make

if [[ $($DETECTORPATH/bin/pythondetector $REQUIRED) \
!= "minimum version installed" ]]; then
    echo "Installing python"
    mkdir -p $DETECTORPATH/temp && cd $DETECTORPATH/temp
    sudo apt update && sudo apt install -y \
    git zlib1g-dev libffi-dev libssl-dev libbz2-dev \
    libncursesw5-dev libgdbm-dev liblzma-dev libsqlite3-dev \
    tk-dev uuid-dev libreadline-dev
    git clone https://github.com/python/cpython.git
    cd cpython
    git checkout $VERSION
    make clean
    ./configure --enable-optimizations
    make
    sudo make install
else
    echo "Minimum python version installed"
fi
