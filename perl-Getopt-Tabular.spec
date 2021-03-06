Name:           perl-Getopt-Tabular
Version:        0.3
Release:        2%{?dist}
Summary:        Table-driven argument parsing for Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Getopt-Tabular/
Source0:        http://www.cpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Getopt::Tabular is a Perl module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv.  All you really need
to do to use the package is set up a table describing all your command-line
options, and call &GetOptions.

%prep
%setup -q -n Getopt-Tabular-%{version}
sed -i 's#/usr/local/bin/perl5#%{__perl}#' demo
chmod a-x demo

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes demo README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.3-2
- clean-up following review, simplify description.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.3-1
- Specfile autogenerated by cpanspec 1.78.
