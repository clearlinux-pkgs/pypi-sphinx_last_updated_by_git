#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_last_updated_by_git
Version  : 0.3.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/0b/10/254205fc4be9b8bbf960b07a6eaf3f17d601a45d4e71804e67db2c3002d7/sphinx-last-updated-by-git-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/10/254205fc4be9b8bbf960b07a6eaf3f17d601a45d4e71804e67db2c3002d7/sphinx-last-updated-by-git-0.3.2.tar.gz
Summary  : Get the "last updated" time for each Sphinx page from Git
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinx_last_updated_by_git-python = %{version}-%{release}
Requires: pypi-sphinx_last_updated_by_git-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(sphinx)

%description
Get the "last updated" time for each Sphinx page from Git
=========================================================

%package python
Summary: python components for the pypi-sphinx_last_updated_by_git package.
Group: Default
Requires: pypi-sphinx_last_updated_by_git-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_last_updated_by_git package.


%package python3
Summary: python3 components for the pypi-sphinx_last_updated_by_git package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_last_updated_by_git)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinx_last_updated_by_git package.


%prep
%setup -q -n sphinx-last-updated-by-git-0.3.2
cd %{_builddir}/sphinx-last-updated-by-git-0.3.2
pushd ..
cp -a sphinx-last-updated-by-git-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656370029
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
