%define upstream_name	 Cflow
%define upstream_version 1.053

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	12

Summary:	Find ``interesting'' flows in raw IP flow files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://net.doit.wisc.edu/~plonka/%{upstream_name}/
Source0:	http://net.doit.wisc.edu/~plonka/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorarch}/auto/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}.pm
%{_mandir}/man?/*
%{_bindir}/flowdumper


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.53.0-10
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.53.0-9
+ Revision: 680772
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.53.0-8mdv2011.0
+ Revision: 555691
- rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.53.0-7mdv2010.1
+ Revision: 505421
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.053-6mdv2010.0
+ Revision: 430293
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.053-5mdv2009.0
+ Revision: 255673
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 1.053-3mdv2008.1
+ Revision: 151852
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.053-2mdv2008.1
+ Revision: 137192
- spec cleanup

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.053-1mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.053-1mdv2007.0
+ Revision: 73435
- import perl-Cflow-1.053-1mdv2007.1

* Fri Jul 07 2006 Buchan Milne <bgmilne@obsidian.co.za> 1.053-1mdv2007.0
- first Mandriva package

