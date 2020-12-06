Name:		freebasic
Version:	1.07.1
Release:	2
Summary:	FreeBASIC language compiler
License:	GPL
Group:		Development/Languages/Other
Source:		FreeBASIC-%version-source.tar.xz
Source1:	FreeBASIC-%version-source-bootstrap.tar.xz
Source2:	FB-manual-%version-html.zip
URL: 		http://freebasic.net
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gpm-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXrandr-devel
BuildRequires:  unzip
BuildRequires:  xz
Requires: 	gcc

%description	
FreeBASIC - is a completely free, open-source, BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%package devel
Group:          Development/Languages/Other
Summary:        FreeBasic development files
Requires:       %{name}

%description devel
This package contains development files for FreeBASIC.

%package examples
Group:          Development/Languages/Other
Summary:        FreeBasic examples
Requires:       %{name}
BuildArch:      noarch

%description examples
This package contains examples for FreeBASIC.

%prep
%setup -q -n FreeBASIC-%version-source
tar xJvf %SOURCE1

mkdir doc/html
unzip -q %SOURCE2 -d doc/html
ln -s 00index.html doc/html/index.html

%build
cd FreeBASIC-1.07.1-source-bootstrap
make bootstrap

cd ..
make 'FBC=./FreeBASIC-1.07.1-source-bootstrap/bin/fbc -i ./FreeBASIC-1.07.1-source-bootstrap/inc' \
ENABLE_LIB64=1

%install
mkdir -p %_prefix
%make_install ENABLE_LIB64=1 prefix=%_prefix

# Install man page
install -D doc/fbc.1 %buildroot%_mandir/man1/fbc.1

%files
%defattr(-,root,root)
%doc *.txt doc/html/*
%_bindir/fbc
%_libdir/freebasic
%_mandir/man1/*

%files devel
%defattr(-,root,root)
%_includedir/freebasic

%files examples
%defattr(-,root,root)
%doc examples

%changelog
