Summary:	Small Web Server Hosting ASP.NET
Name:		xsp
Version:	2.10
Release:	%mkrel 1
License:	BSD
Group:		System/Servers
URL:		http://www.mono-project.com/
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
