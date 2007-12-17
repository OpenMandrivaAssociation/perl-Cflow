%define modname	Cflow

Name:		perl-%{modname}
Version:	1.053
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Cflow::find - find ``interesting'' flows in raw IP flow files
Source:		http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%{version}.tar.bz2
URL:		http://net.doit.wisc.edu/~plonka/Cflow/
BuildRequires:	perl-devel

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
%setup -q -n %{modname}-%{version}

%build
perl Makefile.PL
%make

%install
rm -Rf %{buildroot}
%makeinstall_std INSTALLSITEARCH=%perl_vendorarch INSTALLSITEBIN=%{_bindir} INSTALLSITEMAN1DIR=%{_mandir}/man3 
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man3
for i in `find %{buildroot}/%{_prefix}/local -type f`
do mv ${i} ${i/local/}
done

%check
make test

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{perl_vendorarch}/auto/%{modname}
%{perl_vendorarch}/auto/%{modname}/*
%{perl_vendorarch}/%{modname}*
%{_mandir}/man?/*
%{_bindir}/flowdumper
%doc README



