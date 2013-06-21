%define module Config-ApacheFormat
%define upstream_version 1.2
Summary: 	Use Apache format config files 
Name: 		perl-%{module}
Version: 	%perl_convert_version 1.2
Release: 	1
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/Config-ApacheFormat-1.2.tar.gz
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
%setup -q -n %{module}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/*



%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.2-8mdv2011.0
+ Revision: 653397
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-7mdv2011.0
+ Revision: 430336
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2-6mdv2009.0
+ Revision: 241189
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-4mdv2008.0
+ Revision: 86186
- rebuild


* Mon Jul 25 2005 Olivier Thauvin <nanardon@mandriva.org> 1.2-3mdk
- Add changelog for -2mdk

* Mon Jul 25 2005 Olivier Thauvin <nanardon@mandriva.org> 1.2-2mdk
- Fix {Build}Requires

* Sat Jul 23 2005 Olivier Thauvin <nanardon@mandriva.org> 1.2-1mdk
- first mdk release


