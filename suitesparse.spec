Name:           suitesparse
Version:        5.10.1
Release:        1
Summary:        Sparse Matrix Collection
License:        (LGPLv2+ or BSD) and LGPLv2+ and GPLv2+
URL:            http://faculty.cse.tamu.edu/davis/suitesparse.html
Source0:        http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-%{version}.tar.gz
BuildRequires:  gcc-c++ openblas-devel tbb-devel hardlink lapack-devel openblas-devel metis-devel
Obsoletes:      umfpack <= 5.0.1 ufsparse <= 2.1.1
Provides:       ufsparse = %{version}-%{release}

%description
SuiteSparse is a suite of sparse matrix algorithms.The package includes the following libraries:
  AMD                 approximate minimum degree ordering
  BTF                 permutation to block triangular form (beta)
  CAMD                constrained approximate minimum degree ordering
  COLAMD              column approximate minimum degree ordering
  CCOLAMD             constrained column approximate minimum degree ordering
  CHOLMOD             sparse Cholesky factorization
  CSparse             a concise sparse matrix package
  CXSparse            CSparse extended: complex matrix, int and long int support
  KLU                 sparse LU factorization, primarily for circuit simulation
  LDL                 a simple LDL factorization
  SQPR                a multithread, multifrontal, rank-revealing sparse QR
                      factorization method
  UMFPACK             sparse LU factorization
  SuiteSparse_config  configuration file for all the above packages.
  RBio                read/write files in Rutherford/Boeing format

%package        devel
Summary:        Development files for the suitesparse library
Requires:       %{name} = %{version}-%{release}
Provides:       ufsparse-devel = %{version}-%{release} ufsparse-static = %{version}-%{release} suitesparse-static = %{version}-%{release}
Obsoletes:      umfpack-devel <= 5.0.1 ufsparse-devel <= 2.1.1 suitesparse-static < %{version}-%{release}

%description    devel
The suitesparse-devel package includes header files and libraries necessary for the suitesparse library.

%package        help
Summary:        This package contains help documents
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       suitesparse-doc = %{version}-%{release}
Obsoletes:      suitesparse-doc < %{version}-%{release}

%description    help
Files for help with suitesparse.

%prep
%autosetup -n SuiteSparse-%{version} -p1
rm -r metis*
ln -s %{_includedir}/metis/*.h include/
for fil in $(grep -Frl 'pragma ivdep' .); do
  sed -i.orig 's/pragma ivdep/pragma GCC ivdep/' $fil
  touch -r ${fil}.orig $fil
  rm -f ${fil}.orig
done

sed -i -e '/^  CF =/ s/ -O3 -fexceptions//' SuiteSparse_config/SuiteSparse_config.mk

%build
export AUTOCC=no
export CC=gcc
install -d Doc/{AMD,BTF,CAMD,CCOLAMD,CHOLMOD,COLAMD,KLU,LDL,UMFPACK,SPQR,RBio} Lib Include
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/metis"
export LAPACK=""
export BLAS=-lopenblas
pushd SuiteSparse_config
  %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  ar x libsuitesparseconfig.a
  cp -a *.a ../Lib
  cp -p *.h ../Include
popd

pushd AMD
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License.txt Doc/lesser.txt Doc/ChangeLog Doc/*.pdf ../Doc/AMD
popd

pushd BTF
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/BTF
popd

pushd CAMD
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License.txt Doc/*.pdf ../Doc/CAMD
popd

pushd CCOLAMD
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/CCOLAMD
popd

pushd COLAMD
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/COLAMD
popd

pushd CHOLMOD
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/*.pdf ../Doc/CHOLMOD
  cp -p Cholesky/lesser.txt ../Doc/CHOLMOD/Cholesky_License.txt
  cp -p Core/lesser.txt ../Doc/CHOLMOD/Core_License.txt
  cp -p MatrixOps/gpl.txt ../Doc/CHOLMOD/MatrixOps_License.txt
  cp -p Partition/lesser.txt ../Doc/CHOLMOD/Partition_License.txt
  cp -p Supernodal/gpl.txt ../Doc/CHOLMOD/Supernodal_License.txt
popd

pushd CXSparse
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/cs.h ../Include
  mkdir ../Doc/CXSparse/
  cp -p Doc/* ../Doc/CXSparse
popd

pushd KLU
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/lesser.txt ../Doc/KLU
popd

pushd LDL
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/lesser.txt Doc/*.pdf ../Doc/LDL
popd

pushd UMFPACK
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License.txt Doc/ChangeLog Doc/gpl.txt Doc/*.pdf ../Doc/UMFPACK
popd

pushd SPQR
  pushd Lib
    %make_build CFLAGS="$CFLAGS -DHAVE_TBB -DNPARTITION" TBB=-ltbb BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h* ../Include
  cp -p README{,_SPQR}.txt
  cp -p README_SPQR.txt Doc/* ../Doc/SPQR
popd

pushd RBio
  pushd Lib
    %make_build CFLAGS="$CFLAGS" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX"
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License.txt ../Doc/RBio
popd

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/%{name}
cp -a Include/*.{h,hpp} ${RPM_BUILD_ROOT}%{_includedir}/%{name}/
cp -a Lib/*.a */Lib/*.a lib/*.so* ${RPM_BUILD_ROOT}%{_libdir}/
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/*.so.*
rm -rf Licenses
mkdir Licenses
find */ -iname lesser.txt -o -iname lesserv3.txt -o -iname license.txt -o \
    -iname gpl.txt -o -iname GPLv2.txt -o -iname license \
    -a -not -type d | while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "./Licenses/$b/$x"
    done
hardlink -cv Docs/ Licenses/

%check
export AUTOCC=no
export CC=gcc
TESTDIRS="AMD CAMD CCOLAMD CHOLMOD COLAMD KLU LDL SPQR RBio UMFPACK"
TESTDIRS="$TESTDIRS CXSparse"
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/metis"
export LAPACK=""
export BLAS=-lopenblas 
for d in $TESTDIRS ; do
    %make_build -C $d/Demo CFLAGS="$CFLAGS" LIB="%{?__global_ldflags} -lm -lrt" BLAS="$BLAS" LIBRARY_SUFFIX="$LIBRARY_SUFFIX" SPQR_CONFIG=-DHAVE_TBB TBB=-ltbb
done
 

%files
%doc Licenses
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/suitesparse
%{_libdir}/lib*.so
%{_libdir}/lib*.a

%files help
%doc Doc/*

%changelog
* Thu May 19 2022 baizhonggui <baizhonggui@h-partners.com> - 5.10.1-1
- Upgrade to version 5.10.1

* Mon Dec 23 2019 gulining<gulining1@huawei.com> - 4.4.6-17
- Pakcage init
