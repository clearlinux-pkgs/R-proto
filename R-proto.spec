#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-proto
Version  : 0.3
Release  : 24
URL      : http://cran.r-project.org/src/contrib/proto_0.3-10.tar.gz
Source0  : http://cran.r-project.org/src/contrib/proto_0.3-10.tar.gz
Summary  : Prototype object-based programming
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
Proto is an R package that facilitates prototype
programming, a type of object-oriented programming that
does not use classes as an atomic concept (but is powerful
enough to encompass them).

%prep
%setup -q -c -n proto

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library proto
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library proto


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/proto/DESCRIPTION
/usr/lib64/R/library/proto/FAQ
/usr/lib64/R/library/proto/INDEX
/usr/lib64/R/library/proto/Meta/Rd.rds
/usr/lib64/R/library/proto/Meta/demo.rds
/usr/lib64/R/library/proto/Meta/hsearch.rds
/usr/lib64/R/library/proto/Meta/links.rds
/usr/lib64/R/library/proto/Meta/nsInfo.rds
/usr/lib64/R/library/proto/Meta/package.rds
/usr/lib64/R/library/proto/Meta/vignette.rds
/usr/lib64/R/library/proto/NAMESPACE
/usr/lib64/R/library/proto/NEWS
/usr/lib64/R/library/proto/R/proto
/usr/lib64/R/library/proto/R/proto.rdb
/usr/lib64/R/library/proto/R/proto.rdx
/usr/lib64/R/library/proto/README
/usr/lib64/R/library/proto/THANKS
/usr/lib64/R/library/proto/WISHLIST
/usr/lib64/R/library/proto/demo/proto-vignette.R
/usr/lib64/R/library/proto/demo/proto.R
/usr/lib64/R/library/proto/doc/index.html
/usr/lib64/R/library/proto/doc/proto.Rnw
/usr/lib64/R/library/proto/doc/proto.pdf
/usr/lib64/R/library/proto/doc/protoref.Rnw
/usr/lib64/R/library/proto/doc/protoref.pdf
/usr/lib64/R/library/proto/help/AnIndex
/usr/lib64/R/library/proto/help/aliases.rds
/usr/lib64/R/library/proto/help/paths.rds
/usr/lib64/R/library/proto/help/proto.rdb
/usr/lib64/R/library/proto/help/proto.rdx
/usr/lib64/R/library/proto/html/00Index.html
/usr/lib64/R/library/proto/html/R.css
