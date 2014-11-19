Name:           perl-Business-ISSN
Version:        0.91
Release:        2%{?dist}
Summary:        Perl extension for International Standard Serial Numbers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Business-ISSN/
Source0:        http://www.cpan.org/authors/id/B/BD/BDFOY/Business-ISSN-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl extension for International Standard Serial Numbers

%prep
%setup -q -n Business-ISSN-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.91-2
- Replace nonsense autogenerated description (just use summary).

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.91-1
- Specfile autogenerated by cpanspec 1.78.
