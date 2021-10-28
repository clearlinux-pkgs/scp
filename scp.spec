#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scp
Version  : 0.14.1
Release  : 17
URL      : https://files.pythonhosted.org/packages/1d/b4/1d471ed28e5c044c0e9349ff205740606b5ccdce3371e1fc5697d1e55acb/scp-0.14.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1d/b4/1d471ed28e5c044c0e9349ff205740606b5ccdce3371e1fc5697d1e55acb/scp-0.14.1.tar.gz
Summary  : scp module for paramiko
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: scp-license = %{version}-%{release}
Requires: scp-python = %{version}-%{release}
Requires: scp-python3 = %{version}-%{release}
Requires: paramiko
BuildRequires : buildreq-distutils3
BuildRequires : paramiko

%description
======================
        
        The scp.py module uses a paramiko transport to send and recieve files via the
        scp1 protocol. This is the protocol as referenced from the openssh scp program,
        and has only been tested with this implementation.
        
        
        Example
        -------

%package license
Summary: license components for the scp package.
Group: Default

%description license
license components for the scp package.


%package python
Summary: python components for the scp package.
Group: Default
Requires: scp-python3 = %{version}-%{release}

%description python
python components for the scp package.


%package python3
Summary: python3 components for the scp package.
Group: Default
Requires: python3-core
Provides: pypi(scp)
Requires: pypi(paramiko)

%description python3
python3 components for the scp package.


%prep
%setup -q -n scp-0.14.1
cd %{_builddir}/scp-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631726928
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scp
cp %{_builddir}/scp-0.14.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/scp/a393ab05655034ea1176ada5f33586112407ff71
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scp/a393ab05655034ea1176ada5f33586112407ff71

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
