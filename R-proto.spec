#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-proto
Version  : 1.0.0
Release  : 77
URL      : https://cran.r-project.org/src/contrib/proto_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/proto_1.0.0.tar.gz
Summary  : Prototype Object-Based Programming
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
called prototype-based, rather than class-based object oriented ideas.

%prep
%setup -q -c -n proto
cd %{_builddir}/proto

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589537497

%install
export SOURCE_DATE_EPOCH=1589537497
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proto
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proto
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proto
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc proto || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/proto/DESCRIPTION
/usr/lib64/R/library/proto/FAQ
/usr/lib64/R/library/proto/INDEX
/usr/lib64/R/library/proto/Meta/Rd.rds
/usr/lib64/R/library/proto/Meta/demo.rds
/usr/lib64/R/library/proto/Meta/features.rds
/usr/lib64/R/library/proto/Meta/hsearch.rds
/usr/lib64/R/library/proto/Meta/links.rds
/usr/lib64/R/library/proto/Meta/nsInfo.rds
/usr/lib64/R/library/proto/Meta/package.rds
/usr/lib64/R/library/proto/Meta/vignette.rds
/usr/lib64/R/library/proto/NAMESPACE
/usr/lib64/R/library/proto/NEWS.md
/usr/lib64/R/library/proto/R/proto
/usr/lib64/R/library/proto/R/proto.rdb
/usr/lib64/R/library/proto/R/proto.rdx
/usr/lib64/R/library/proto/ReleaseNotes.txt
/usr/lib64/R/library/proto/THANKS
/usr/lib64/R/library/proto/WISHLIST
/usr/lib64/R/library/proto/demo/proto-gWidgets.R
/usr/lib64/R/library/proto/demo/proto-vignette.R
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
/usr/lib64/R/library/proto/tests/testthat.R
/usr/lib64/R/library/proto/tests/testthat/test-getting.R
/usr/lib64/R/library/proto/tests/testthat/test-printing.R
