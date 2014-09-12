#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooseX
%define		pnam	Object-Pluggable
%include	/usr/lib/rpm/macros.perl
Summary:	MooseX::Object::Pluggable - Make your classes pluggable
Name:		perl-MooseX-Object-Pluggable
Version:	0.0011
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce3b5ffc6d05bdd77102488a85e401d1
URL:		http://search.cpan.org/dist/MooseX-Object-Pluggable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.35
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is meant to be loaded as a role from Moose-based classes
it will add five methods and four attributes to assist you with the
loading and handling of plugins and extensions for plugins. I
understand that this may pollute your namespace, however I took great
care in using the least ambiguous names possible.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MooseX/Object
%{perl_vendorlib}/MooseX/Object/*.pm
%{_mandir}/man3/*
