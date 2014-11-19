Name:           perl-Config-AutoConf
Version:        0.305
Release:        2%{?dist}
Summary:        Config::AutoConf Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-AutoConf/
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/Config-AutoConf-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util) >= 1.18
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Text::ParseWords)
Requires:       perl(Capture::Tiny)
Requires:       perl(Carp)
Requires:       perl(Cwd)
Requires:       perl(Exporter)
Requires:       perl(ExtUtils::CBuilder) >= 0.23
Requires:       perl(File::Slurp::Tiny)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(Scalar::Util) >= 1.18
Requires:       perl(Text::ParseWords)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A module to implement some of AutoConf macros in pure perl.

%prep
%setup -q -n Config-AutoConf-%{version}

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
* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.305-2
- Update description from cpan.

* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.305-1
- Specfile autogenerated by cpanspec 1.78.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.19-1
- Specfile autogenerated by cpanspec 1.78.
