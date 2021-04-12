#!/usr/bin/tclsh

set arch "x86_64"
set version "1.07.3"

set fileurl "https://pilotfiber.dl.sourceforge.net/project/fbc/FreeBASIC-1.07.3/Documentation/FB-manual-$version-html.zip"
set var [list wget $fileurl -O FB-manual-$version-html.zip]
exec >@stdout 2>@stderr {*}$var

set fileurl "https://pilotfiber.dl.sourceforge.net/project/fbc/FreeBASIC-1.07.3/Source/FreeBASIC-$version-source.tar.xz"
set var [list wget $fileurl -O FreeBASIC-$version-source.tar.xz]
exec >@stdout 2>@stderr {*}$var

set fileurl "https://pilotfiber.dl.sourceforge.net/project/fbc/FreeBASIC-1.07.3/Source/FreeBASIC-$version-source-bootstrap.tar.xz"
set var [list wget $fileurl -O FreeBASIC-$version-source-bootstrap.tar.xz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force FreeBASIC-$version-source.tar.xz build/SOURCES
file copy -force FreeBASIC-$version-source-bootstrap.tar.xz build/SOURCES
file copy -force FB-manual-$version-html.zip build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb freebasic.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force FreeBASIC-$version-source.tar.xz
file delete -force FreeBASIC-$version-source-bootstrap.tar.xz
file delete -force FB-manual-$version-html.zip

