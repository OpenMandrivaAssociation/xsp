Summary:	Small Web Server Hosting ASP.NET
Name:		xsp
Version:	2.10.2
Release:	2
License:	BSD
Group:		System/Servers
URL:		https://www.mono-project.com/
Source:	 http://go-mono.com/sources/xsp/xsp-%{version}.tar.bz2
BuildRequires:	mono-devel
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts: apache-mod_mono < 1:1.2.5-2

%description
The XSP server is a small Web server that hosts the Mono System.Web
classes for running what is commonly known as ASP.NET.

%package devel
Group:		Development/Other
Summary:	Development files for %name
Requires:	%name = %version-%release

%description devel
The XSP server is a small Web server that hosts the Mono System.Web
classes for running what is commonly known as ASP.NET.

This package contains the development parts of %{name}.

%package doc
Summary:	Development documentation for %name
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %name in
  Monodoc format.

%prep

%setup -q 

%build
./configure --prefix=%_prefix
make

%install
rm -fr %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig
#gw install manually:
install -D src/Mono.WebServer.XSP/xsp.pc %buildroot%_datadir/pkgconfig/xsp.pc
# strip away annoying ^M
find %{buildroot} -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find %{buildroot} -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
#gw remove unit tests
rm -rf %buildroot%_prefix/lib/xsp/unittests
   
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
		    
%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL NEWS README COPYING
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%dir %_prefix/lib/xsp
%_prefix/lib/xsp/2.0
%_prefix/lib/xsp/4.0
%_prefix/lib/xsp/test
%_prefix/lib/mono/2.0/*
%_prefix/lib/mono/4.0/*
%_prefix/lib/mono/gac/*

%files devel
%defattr(-,root,root)
%_datadir/pkgconfig/xsp.pc
%_datadir/pkgconfig/xsp-2.pc
%_datadir/pkgconfig/xsp-4.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/*


%changelog
* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdv2011.0
+ Revision: 685497
- new version

* Thu Feb 17 2011 Götz Waschk <waschk@mandriva.org> 2.10-1
+ Revision: 638113
- update to new version 2.10

* Thu Jan 06 2011 Götz Waschk <waschk@mandriva.org> 2.8.2-1mdv2011.0
+ Revision: 629042
- update to new version 2.8.2

* Thu Dec 23 2010 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdv2011.0
+ Revision: 624030
- new version
- update file list
- split out devel package
- remove unit tests

* Thu Oct 07 2010 Götz Waschk <waschk@mandriva.org> 2.8-1mdv2011.0
+ Revision: 583937
- new version
- update file list
- manually install pkgconfig file
- add doc package

* Tue Jul 20 2010 Götz Waschk <waschk@mandriva.org> 2.6.5-1mdv2011.0
+ Revision: 555672
- update to new version 2.6.5

* Wed Apr 28 2010 Götz Waschk <waschk@mandriva.org> 2.6.4-1mdv2010.1
+ Revision: 539981
- update to new version 2.6.4

* Tue Mar 16 2010 Götz Waschk <waschk@mandriva.org> 2.6.3-1mdv2010.1
+ Revision: 521497
- update to new version 2.6.3

* Tue Dec 15 2009 Götz Waschk <waschk@mandriva.org> 2.6-1mdv2010.1
+ Revision: 478864
- update to new version 2.6

* Thu Dec 10 2009 Götz Waschk <waschk@mandriva.org> 2.4.3-1mdv2010.1
+ Revision: 475950
- update to new version 2.4.3

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 2.4.2-1mdv2010.0
+ Revision: 390910
- update to new version 2.4.2

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2010.0
+ Revision: 368972
- new version
- update file list

* Wed Jan 14 2009 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2009.1
+ Revision: 329392
- new version
- update file list

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 291912
- new version

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.9.1-2mdv2009.0
+ Revision: 269844
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Götz Waschk <waschk@mandriva.org> 1.9.1-1mdv2009.0
+ Revision: 196541
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 1.9-1mdv2009.0
+ Revision: 192398
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2008.1
+ Revision: 119272
- new version
- update file list

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2008.0
+ Revision: 80101
- remove build workaround
- stand alone package of xsp
- copy apache-mod_mono to xsp

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.5-1mdv2008.0
+ Revision: 75587
- new version

* Fri Aug 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-3mdv2008.0
+ Revision: 64723
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed May 16 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.4-1mdv2008.0
+ Revision: 27355
- new version

