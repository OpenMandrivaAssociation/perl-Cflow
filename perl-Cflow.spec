%define module	Cflow

Name:		perl-%{module}
Version:	1.053
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Find ``interesting'' flows in raw IP flow files
Source:		http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.bz2
URL:		http://net.doit.wisc.edu/~plonka/Cflow/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package is of little use on its own. It requires input in the form of
time-stamped raw flow files produced by other software packages. These ``flow
sources'' either snoop a local ethernet (via libpcap) or collect flow
information from IP routers that are configured to export said information. The
following flow sources are supported:

argus by Carter Bullard: 
   http://www.qosient.com/argus/

flow-tools by Mark Fullmer (with NetFlow v1, v5, v6, or v7):
   http://www.splintered.net/sw/flow-tools/

CAIDA's cflowd (with NetFlow v5):
   http://www.caida.org/tools/measurement/cflowd/
   http://net.doit.wisc.edu/~plonka/cflowd/

lfapd by Steve Premeau (with LFAPv4):
   http://www.nmops.org/


%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%check
make test

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/%{module}
%{perl_vendorarch}/%{module}.pm
%{_mandir}/man?/*
%{_bindir}/flowdumper
