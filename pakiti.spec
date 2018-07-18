Summary:	Patching status monitoring tool
Name:		pakiti-client
Version:	X
Release:	1%{?dist}
URL:		https://github.com/CESNET/pakiti-client
License:	ASL 2.0
Group:		Applications/Internet
Source0:	%{url}/archive/v%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
BuildRequires:	perl
Requires:	openssl perl perl-LWP-Protocol-https

%description
Pakiti provides a monitoring mechanism to check the patching status of
Linux systems.

This package provides the client part that is able to send information
about installed software to a defined Pakiti server.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
install -D -m755 pakiti-client   %{buildroot}%{_bindir}/pakiti-client
install -D -m644 pakiti-client.1 %{buildroot}%{_mandir}/man1/pakiti-client.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man?/*

#%changelog
# See debian/changelog
