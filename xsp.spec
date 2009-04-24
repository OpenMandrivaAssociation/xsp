Summary:	Small Web Server Hosting ASP.NET
Name:		xsp
Version:	2.4
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

%prep

%setup -q 

%build
./configure --prefix=%_prefix
make

%install
rm -fr %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

# strip away annoying ^M
find %{buildroot} -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find %{buildroot} -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
   
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
		    
%files
%defattr(-,root,root)
%doc AUTHORS INSTALL NEWS README COPYING
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%_datadir/pkgconfig/xsp.pc
%_datadir/pkgconfig/xsp-2.pc
%dir %_prefix/lib/xsp
%_prefix/lib/xsp/1.0
%_prefix/lib/xsp/2.0
%_prefix/lib/xsp/test
%_prefix/lib/xsp/unittests
%_prefix/lib/mono/1.0/*
%_prefix/lib/mono/2.0/*
%_prefix/lib/mono/gac/*
