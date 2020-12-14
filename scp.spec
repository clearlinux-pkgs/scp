#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scp
Version  : 0.13.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/05/e0/ac4169e773e12a08d941ca3c006cb8c91bee9d6d80328a15af850b5e7480/scp-0.13.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/e0/ac4169e773e12a08d941ca3c006cb8c91bee9d6d80328a15af850b5e7480/scp-0.13.2.tar.gz
Summary  : scp module for paramiko
Group    : Development/Tools
License  : LGPL-2.1
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
%setup -q -n scp-0.13.2
cd %{_builddir}/scp-0.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588710429
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scp
cp %{_builddir}/scp-0.13.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/scp/a393ab05655034ea1176ada5f33586112407ff71
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
