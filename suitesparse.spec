Name:           suitesparse
Version:        4.4.6
Release:        17
Summary:        Sparse Matrix Collection
License:        (LGPLv2+ or BSD) and LGPLv2+ and GPLv2+
URL:            http://faculty.cse.tamu.edu/davis/suitesparse.html
Source0:        http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-%{version}.tar.gz
BuildRequires:  gcc-c++ openblas-devel tbb-devel hardlink
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
%autosetup -n SuiteSparse -p1
for fil in $(grep -Frl 'pragma ivdep' .); do
  sed -i 's/pragma ivdep/pragma GCC ivdep/' $fil
done
sed -i '/^  CF =/ s/ -O3 -fexceptions//' SuiteSparse_config/SuiteSparse_config.mk

%build
install -d Doc/{AMD,BTF,CAMD,CCOLAMD,CHOLMOD,COLAMD,KLU,LDL,UMFPACK,SPQR,RBio} Lib Include
cd SuiteSparse_config
  %make_build CFLAGS="$RPM_OPT_FLAGS"
  ar x libsuitesparseconfig.a
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libsuitesparseconfig.so.4 -o libsuitesparseconfig.so.4.4.4 ../SuiteSparse_config/*.o -lm
    ln -sf libsuitesparseconfig.so.4.4.4 libsuitesparseconfig.so.4
    ln -sf libsuitesparseconfig.so.4.4.4 libsuitesparseconfig.so
    install -D ../SuiteSparse_config/*.a ./
  cd ../SuiteSparse_config
  install -D *.h ../Include
cd ..

cd AMD
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libamd.so.2 -o libamd.so.2.4.1 ../AMD/Lib/*.o libsuitesparseconfig.so.4 -lm
    ln -sf libamd.so.2.4.1 libamd.so.2
    ln -sf libamd.so.2.4.1 libamd.so
    install -D ../AMD/Lib/*.a ./
  cd ../AMD
  install -D Include/*.h ../Include
  install -D README.txt Doc/License.txt Doc/lesser.txt Doc/ChangeLog Doc/*.pdf ../Doc/AMD
cd ..

cd BTF
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libbtf.so.1 -o libbtf.so.1.2.1 ../BTF/Lib/*.o
    ln -sf libbtf.so.1.2.1 libbtf.so.1
    ln -sf libbtf.so.1.2.1 libbtf.so
    install -D ../BTF/Lib/*.a ./
  cd ../BTF
  install -D Include/*.h ../Include
  install -D README.txt Doc/* ../Doc/BTF
cd ..

cd CAMD
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcamd.so.2 -o libcamd.so.2.4.1 ../CAMD/Lib/*.o libsuitesparseconfig.so.4 -lm
    ln -sf libcamd.so.2.4.1 libcamd.so.2
    ln -sf libcamd.so.2.4.1 libcamd.so
    install -D ../CAMD/Lib/*.a ./
  cd ../CAMD
  install -D Include/*.h ../Include
  install -D README.txt Doc/ChangeLog Doc/License Doc/*.pdf ../Doc/CAMD
cd ..

cd CCOLAMD
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libccolamd.so.2 -o libccolamd.so.2.9.1 ../CCOLAMD/Lib/*.o libsuitesparseconfig.so.4 -lm
    ln -sf libccolamd.so.2.9.1 libccolamd.so.2
    ln -sf libccolamd.so.2.9.1 libccolamd.so
    install -D ../CCOLAMD/Lib/*.a ./
  cd ../CCOLAMD
  install -D Include/*.h ../Include
  install -D README.txt Doc/* ../Doc/CCOLAMD
cd ..

cd COLAMD
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcolamd.so.2 -o libcolamd.so.2.9.1 ../COLAMD/Lib/*.o libsuitesparseconfig.so.4 -lm
    ln -sf libcolamd.so.2.9.1 libcolamd.so.2
    ln -sf libcolamd.so.2.9.1 libcolamd.so
    install -D ../COLAMD/Lib/*.a ./
  cd ../COLAMD
  install -D Include/*.h ../Include
  install -D README.txt Doc/* ../Doc/COLAMD
cd ..

CHOLMOD_FLAGS="$RPM_OPT_FLAGS -DNPARTITION"
cd CHOLMOD
  cd Lib
    %make_build CFLAGS="$CHOLMOD_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcholmod.so.3 -o libcholmod.so.3.0.6 ../CHOLMOD/Lib/*.o \
        -lopenblas libamd.so.2 libcamd.so.2 libcolamd.so.2 libccolamd.so.2 libsuitesparseconfig.so.4 -lm
    ln -sf libcholmod.so.3.0.6 libcholmod.so.3
    ln -sf libcholmod.so.3.0.6 libcholmod.so
    install -D ../CHOLMOD/Lib/*.a ./
  cd ../CHOLMOD
  install -D Include/*.h ../Include
  install -D README.txt Doc/*.pdf ../Doc/CHOLMOD
  install -D Cholesky/License.txt ../Doc/CHOLMOD/Cholesky_License.txt
  install -D Core/License.txt ../Doc/CHOLMOD/Core_License.txt
  install -D MatrixOps/License.txt ../Doc/CHOLMOD/MatrixOps_License.txt
  install -D Partition/License.txt ../Doc/CHOLMOD/Partition_License.txt
  install -D Supernodal/License.txt ../Doc/CHOLMOD/Supernodal_License.txt
cd ..

cd CXSparse
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcxsparse.so.3 -o libcxsparse.so.3.1.4 ../CXSparse/Lib/*.o -lm
    ln -sf libcxsparse.so.3.1.4 libcxsparse.so.3
    ln -sf libcxsparse.so.3.1.4 libcxsparse.so
    install -D ../CXSparse/Lib/*.a ./
  cd ../CXSparse
  install -D Include/cs.h ../Include
  install -d ../Doc/CXSparse/
  install -D Doc/* ../Doc/CXSparse
cd ..

cd KLU
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libklu.so.1 -o libklu.so.1.3.3 ../KLU/Lib/*.o \
        libamd.so.2 libcolamd.so.2 libbtf.so.1 libsuitesparseconfig.so.4
    ln -sf libklu.so.1.3.3 libklu.so.1
    ln -sf libklu.so.1.3.3 libklu.so
    install -D ../KLU/Lib/*.a ./
  cd ../KLU
  install -D Include/*.h ../Include
  install -D README.txt Doc/lesser.txt ../Doc/KLU
cd ..

cd LDL
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libldl.so.2 -o libldl.so.2.2.1 ../LDL/Lib/*.o
    ln -sf libldl.so.2.2.1 libldl.so.2
    ln -sf libldl.so.2.2.1 libldl.so
    install -D ../LDL/Lib/*.a ./
  cd ../LDL
  install -D Include/*.h ../Include
  install -D README.txt Doc/ChangeLog Doc/lesser.txt Doc/*.pdf ../Doc/LDL
cd ..

cd UMFPACK
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libumfpack.so.5 -o libumfpack.so.5.7.1 ../UMFPACK/Lib/*.o \
        -lopenblas libamd.so.2 libcholmod.so.3 libsuitesparseconfig.so.4 -lm
    ln -sf libumfpack.so.5.7.1 libumfpack.so.5
    ln -sf libumfpack.so.5.7.1 libumfpack.so
    install -D ../UMFPACK/Lib/*.a ./
  cd ../UMFPACK
  install -D Include/*.h ../Include
  install -D README.txt Doc/License Doc/ChangeLog Doc/gpl.txt Doc/*.pdf ../Doc/UMFPACK
cd ..

cd SPQR
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS -DHAVE_TBB -DNPARTITION"
  cd ..
  cd ../Lib
    g++ -shared %{?__global_ldflags} -Wl,-soname,libspqr.so.2 -o libspqr.so.2.0.1 ../SPQR/Lib/*.o \
        -lopenblas -ltbb libcholmod.so.3 libsuitesparseconfig.so.4 -lm
    ln -sf libspqr.so.2.0.1 libspqr.so.2
    ln -sf libspqr.so.2.0.1 libspqr.so
    install -D ../SPQR/Lib/*.a ./
  cd ../SPQR
  install -D Include/*.h* ../Include
  install -D README{,_SPQR}.txt
  install -D README_SPQR.txt Doc/* ../Doc/SPQR
cd ..

cd RBio
  cd Lib
    %make_build CFLAGS="$RPM_OPT_FLAGS"
  cd ..
  cd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,librbio.so.2 -o \
        librbio.so.2.2.1 ../RBio/Lib/*.o libsuitesparseconfig.so.4
    ln -sf librbio.so.2.2.1 librbio.so.2
    ln -sf librbio.so.2.2.1 librbio.so
    install -D ../RBio/Lib/*.a ./
  cd ../RBio
  install -D Include/*.h ../Include
  install -D README.txt Doc/ChangeLog Doc/License.txt ../Doc/RBio
cd ..

%install
install -d ${RPM_BUILD_ROOT}%{_libdir}
install -d ${RPM_BUILD_ROOT}%{_includedir}/%{name}
cd Lib
  for f in *.a *.so*; do
    cp -a $f ${RPM_BUILD_ROOT}%{_libdir}/$f
  done
cd ..
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/*.so.*
cd Include
  for f in *.h *.hpp;  do
    cp -a $f ${RPM_BUILD_ROOT}%{_includedir}/%{name}/$f
  done
cd ..
rm -rf Licenses
install -d Licenses
find */ -iname lesser.txt -o -iname license.txt -o -iname gpl.txt -o -iname license | while read f
    do
        b="${f%%/*}";r="${f#$b}";x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "./Licenses/$b/$x"
    done
hardlink -cv Docs/ Licenses/

%check
TESTDIRS="AMD CAMD CCOLAMD CHOLMOD COLAMD KLU LDL SPQR RBio UMFPACK CXSparse"
for d in $TESTDIRS ; do
    make -C $d/Demo CFLAGS="$RPM_OPT_FLAGS" LAPACK="" SPQR_CONFIG=-DHAVE_TBB TBB=-ltbb
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
* Mon Dec 23 2019 gulining<gulining1@huawei.com> - 4.4.6-17
- Pakcage init
