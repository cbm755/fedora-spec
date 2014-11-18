Name:           perl-XML-Writer-String
Version:        0.1
Release:        3%{?dist}
Summary:        Capture output from XML::Writer
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Writer-String/
Source0:        http://www.cpan.org/authors/id/S/SO/SOLIVER/XML-Writer-String-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements a bare-bones class specifically for the purpose of
capturing data from the XML::Writer module. XML::Writer expects an
IO::Handle object and writes XML data to the specified object (or STDOUT)
via it's print() method. This module simulates such an object for the
specific purpose of providing the required print() method.

%prep
%setup -q -n XML-Writer-String-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 18 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.1-3
- rev bump to force copr rebuild on Fedora 21.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.1-1
- Specfile autogenerated by cpanspec 1.78.
