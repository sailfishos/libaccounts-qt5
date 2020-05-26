Name:           libaccounts-qt5
Version:        1.13
Release:        1
License:        LGPLv2
Summary:        Accounts framework (Qt binding)
Url:            https://gitlab.com/accounts-sso/libaccounts-qt
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libaccounts-glib) >= 1.24

%description
Framework to provide the accounts.

%package devel
Summary:        Development files for accounts-qt5
Requires:       %{name} = %{version}
Provides:       accounts-qt5-dev

%description devel
Headers and static libraries for the accounts.

%package tests
Summary:        Tests for accounts-qt5
Requires:       %{name} = %{version}

%description tests
Tests for accounts-qt5.

%package doc
Summary:        Documentation for accounts-qt5

%description doc
HTML documentation for the accounts.

%prep
%setup -q -n %{name}-%{version}/libaccounts-qt
sed -i 's,DATA_PATH = .*,DATA_PATH = /opt/tests/%{name}/data,' tests/tst_libaccounts.pro

%build
%qmake5 CONFIG+=release
make %{?_smp_mflags}

%install
INSTALL_LIBDIR=%{buildroot}/%{_libdir} %qmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}-doc-%{version}
cp README.md %{buildroot}%{_docdir}/%{name}-doc-%{version}/README
mkdir -p %{buildroot}/opt/tests/%{name}/data
cp tests/*.provider %{buildroot}/opt/tests/%{name}/data/
cp tests/*.application %{buildroot}/opt/tests/%{name}/data/
cp tests/*.service %{buildroot}/opt/tests/%{name}/data/
cp tests/*.service-type %{buildroot}/opt/tests/%{name}/data/
cp -r tests/applications %{buildroot}/opt/tests/%{name}/data/
mv %{buildroot}/%{_bindir}/accountstest %{buildroot}/opt/tests/%{name}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libaccounts-qt5.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/accounts-qt5/Accounts/Account
%{_includedir}/accounts-qt5/Accounts/AccountService
%{_includedir}/accounts-qt5/Accounts/Application
%{_includedir}/accounts-qt5/Accounts/AuthData
%{_includedir}/accounts-qt5/Accounts/Error
%{_includedir}/accounts-qt5/Accounts/Manager
%{_includedir}/accounts-qt5/Accounts/Provider
%{_includedir}/accounts-qt5/Accounts/Service
%{_includedir}/accounts-qt5/Accounts/ServiceType
%{_includedir}/accounts-qt5/Accounts/*.h
%{_libdir}/libaccounts-qt5.so
%{_libdir}/pkgconfig/accounts-qt5.pc
%{_libdir}/cmake/AccountsQt5/AccountsQt5Config.cmake
%{_libdir}/cmake/AccountsQt5/AccountsQt5ConfigVersion.cmake

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}

%files doc
%defattr(-,root,root,-)
%doc README 
%license COPYING
%{_datadir}/doc/*
