Name:           perl-XML-LibXML-Simple
Version:        0.94
Release:        1%{?dist}
Summary:        XML::LibXML clone of XML::Simple::XMLin()
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-LibXML-Simple/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp::Tiny)
BuildRequires:  perl(Test::More) >= 0.54
BuildRequires:  perl(XML::LibXML) >= 1.64
Requires:       perl(File::Slurp::Tiny)
Requires:       perl(Test::More) >= 0.54
Requires:       perl(XML::LibXML) >= 1.64
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is a blunt rewrite of XML::Simple (by Grant McLean) to use the
XML::LibXML parser for XML structures, where the original uses plain Perl
or SAX parsers.

%prep
%setup -q -n XML-LibXML-Simple-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.94-1
- Specfile autogenerated by cpanspec 1.78.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.91-1
- Specfile autogenerated by cpanspec 1.78.
