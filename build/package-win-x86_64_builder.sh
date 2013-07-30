#!/bin/bash

# Ce script est à exécuter sur la machine virtuelle windows 7

# default values
packageDir="./lastDiyabc"
diyabc_git="../"
MinGw_bindir="/c/MinGW64/bin/"

# custom values
if [[ $# > 0 ]]; then
    packageDir="$1"
fi
if [[ $# > 1 ]]; then
    diyabc_git="$2"
fi
if [[ $# > 2 ]]; then
    MinGw_bindir="$3"
fi

rm -rf $packageDir
cd $diyabc_git

$MinGw_bindir/mingw32-make.exe clean
MFLAGS="-static --enable-lib64" $MinGw_bindir/mingw32-make.exe
cp $MinGw_bindir/*.dll ./gui/data/bin/
cp ./src-JMC-C++/general.exe ./gui/data/bin/diyabc-comput-win-i386
cp ./src-JMC-C++/general.exe ./gui/data/bin/diyabc-comput-win-x64

cd ./build/
./windows_generation.sh -p ./pyinstaller-2.0/pyinstaller.py -i ../gui/data/icons/coccicon.ico -o $packageDir -m ../gui/src/diyabc.py -a 64
cd $packageDir
/c/Program\ Files/7-Zip/7z.exe a "`ls | grep diyabc*64`.zip" diyabc*64
rm -r diyabc*64
