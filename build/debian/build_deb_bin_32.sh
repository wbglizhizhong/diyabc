#!/bin/bash

function printUsage(){
echo "usage : 
build_deb_bin.sh  path_to_makefile  path_to_version.txt

"
}

if [ $# -eq 0 ] ; then
    printUsage
    exit
fi

MAKEPATH=$1
VERSIONFILE=$2
VERSION="`head -n 1 $VERSIONFILE`"

PACKAGEDIR=diyabc-bin\_$VERSION\_i386
rm -rf $PACKAGEDIR

# template copy 
echo $PACKAGEDIR
cp -rp diyabc-bin-pkg-template/ $PACKAGEDIR/

# bin compilation
cd `dirname $MAKEPATH`
make clean
make
cd -
mkdir -p $PACKAGEDIR/usr/bin/
chmod 755 $PACKAGEDIR/usr/bin/
strip ../../src-JMC-C++/general
cp -rp ../../src-JMC-C++/general $PACKAGEDIR/usr/bin/diyabc
chmod 755 $PACKAGEDIR/usr/bin/diyabc  $PACKAGEDIR/usr  $PACKAGEDIR/usr/share  $PACKAGEDIR/usr/share/doc  $PACKAGEDIR/usr/share/doc/diyabc-bin

# package generation

# gestion du man
sed -i "s/BUILDDATE/$BUILDDATE/" $PACKAGEDIR/usr/share/man/man1/diyabc.1
sed -i "s/VersionX/Version $VERSION/" $PACKAGEDIR/usr/share/man/man1/diyabc.1
gzip -9 $PACKAGEDIR/usr/share/man/man1/diyabc.1
chmod 644 $PACKAGEDIR/usr/share/man/man1/diyabc.1.gz
# control file edition
sed -i "s/Version: X/Version: $VERSION/" $PACKAGEDIR/DEBIAN/control
sed -i "s/Architecture: X/Architecture: i386/" $PACKAGEDIR/DEBIAN/control
git log | head -n 100 > $PACKAGEDIR/usr/share/doc/diyabc-bin/changelog
gzip -9 $PACKAGEDIR/usr/share/doc/diyabc-bin/changelog
chmod 644 $PACKAGEDIR/usr/share/doc/diyabc-bin/changelog.gz

cp -r $PACKAGEDIR /tmp
cd /tmp/$PACKAGEDIR
find . -type f ! -regex '.*.hg.*' ! -regex '.*?debian-binary.*' ! -regex '.*?DEBIAN.*' -printf '%P ' | xargs md5sum > DEBIAN/md5sums
cd -
chown -R root:root /tmp/$PACKAGEDIR

dpkg-deb -b /tmp/$PACKAGEDIR
mv /tmp/$PACKAGEDIR.deb ./
rm -rf /tmp/$PACKAGEDIR $PACKAGEDIR
