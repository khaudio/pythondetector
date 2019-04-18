#!/bin/bash

REQUIRED="3.7.0"
DETECTORPATH=$PWD

if [[ $($DETECTORPATH/bin/pythondetector $REQUIRED) != "minimum version installed" ]]; then
    echo "Installing python"
    mkdir -p $DETECTORPATH/temp && cd $DETECTORPATH/temp
    sudo apt install -y git zlib1g-dev libffi-dev libssl-dev libbz2-dev libncursesw5-dev libgdbm-dev liblzma-dev libsqlite3-dev tk-dev uuid-dev libreadline-dev
    git clone git@github.com:python/cpython.git
    cd cpython
    ./configure --enable-optimizations
    make
    sudo make install
fi
