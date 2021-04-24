#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ncbit
Version  : 2013.03.29
Release  : 19
URL      : https://cran.r-project.org/src/contrib/ncbit_2013.03.29.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ncbit_2013.03.29.tar.gz
Summary  : retrieve and build NBCI taxonomic data
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
searchable as an R object

%prep
%setup -q -c -n ncbit
cd %{_builddir}/ncbit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589534259

%install
export SOURCE_DATE_EPOCH=1589534259
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncbit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncbit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncbit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ncbit || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ncbit/DESCRIPTION
/usr/lib64/R/library/ncbit/INDEX
/usr/lib64/R/library/ncbit/Meta/Rd.rds
/usr/lib64/R/library/ncbit/Meta/data.rds
/usr/lib64/R/library/ncbit/Meta/features.rds
/usr/lib64/R/library/ncbit/Meta/hsearch.rds
/usr/lib64/R/library/ncbit/Meta/links.rds
/usr/lib64/R/library/ncbit/Meta/nsInfo.rds
/usr/lib64/R/library/ncbit/Meta/package.rds
/usr/lib64/R/library/ncbit/NAMESPACE
/usr/lib64/R/library/ncbit/R/ncbit
/usr/lib64/R/library/ncbit/R/ncbit.rdb
/usr/lib64/R/library/ncbit/R/ncbit.rdx
/usr/lib64/R/library/ncbit/data/datalist
/usr/lib64/R/library/ncbit/data/ncbi.rda
/usr/lib64/R/library/ncbit/help/AnIndex
/usr/lib64/R/library/ncbit/help/aliases.rds
/usr/lib64/R/library/ncbit/help/ncbit.rdb
/usr/lib64/R/library/ncbit/help/ncbit.rdx
/usr/lib64/R/library/ncbit/help/paths.rds
/usr/lib64/R/library/ncbit/html/00Index.html
/usr/lib64/R/library/ncbit/html/R.css
