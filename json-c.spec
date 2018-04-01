#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : json-c
Version  : 0.13.1
Release  : 11
URL      : https://s3.amazonaws.com/json-c_releases/releases/json-c-0.13.1.tar.gz
Source0  : https://s3.amazonaws.com/json-c_releases/releases/json-c-0.13.1.tar.gz
Summary  : A JSON implementation in C
Group    : Development/Tools
License  : MIT
Requires: json-c-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description


%package dev
Summary: dev components for the json-c package.
Group: Development
Requires: json-c-lib
Provides: json-c-devel

%description dev
dev components for the json-c package.


%package dev32
Summary: dev32 components for the json-c package.
Group: Default
Requires: json-c-lib32
Requires: json-c-dev

%description dev32
dev32 components for the json-c package.


%package lib
Summary: lib components for the json-c package.
Group: Libraries

%description lib
lib components for the json-c package.


%package lib32
Summary: lib32 components for the json-c package.
Group: Default

%description lib32
lib32 components for the json-c package.


%prep
%setup -q -n json-c-0.13.1
pushd ..
cp -a json-c-0.13.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522542694
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522542694
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/json-c/arraylist.h
/usr/include/json-c/bits.h
/usr/include/json-c/debug.h
/usr/include/json-c/json.h
/usr/include/json-c/json_c_version.h
/usr/include/json-c/json_config.h
/usr/include/json-c/json_inttypes.h
/usr/include/json-c/json_object.h
/usr/include/json-c/json_object_iterator.h
/usr/include/json-c/json_pointer.h
/usr/include/json-c/json_tokener.h
/usr/include/json-c/json_util.h
/usr/include/json-c/json_visit.h
/usr/include/json-c/linkhash.h
/usr/include/json-c/printbuf.h
/usr/lib64/libjson-c.so
/usr/lib64/pkgconfig/json-c.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libjson-c.so
/usr/lib32/pkgconfig/32json-c.pc
/usr/lib32/pkgconfig/json-c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjson-c.so.4
/usr/lib64/libjson-c.so.4.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libjson-c.so.4
/usr/lib32/libjson-c.so.4.0.0
