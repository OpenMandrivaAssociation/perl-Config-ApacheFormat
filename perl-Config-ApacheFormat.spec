%define module Config-ApacheFormat
%define name perl-%{module}
%define version 1.2
%define release %mkrel 4

Summary: 	Use Apache format config files 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/%{module}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{module}
BuildRequires: perl-devel
BuildRequires: perl(Class::MethodMaker)
# This one is not found automatically
Requires:      perl(Class::MethodMaker) 
BuildArch: noarch

%description
This module is designed to parse a configuration file in the same syntax used
by the Apache web server (see http://httpd.apache.org for details). This
allows you to build applications which can be easily managed by experienced
Apache admins. Also, by using this module, you'll benefit from the support for
nested blocks with built-in parameter inheritance. This can greatly reduce the
amount or repeated information in your configuration files.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/*

