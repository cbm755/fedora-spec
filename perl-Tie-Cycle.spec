Name:           perl-Tie-Cycle
Version:        1.20
Release:        2%{?dist}
Summary:        Cycle through a list of values via a scalar
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tie-Cycle/
Source0:        http://www.cpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More) >= 0.95
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.95.
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This Perl module can be used to go through a list over and over again.
Once you get to the end of the list, you go back to the beginning.  You
do not have to worry about any of this since the magic of tie does that
for you.

%prep
%setup -q -n Tie-Cycle-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.20-2
- clean-up following review.

* Fri Oct 03 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.20-1
- Specfile autogenerated by cpanspec 1.78
- Manually added Test::Simple dep,
  filed [upstream](https://github.com/briandfoy/tie-cycle/issues/2).

* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.19-1
- Specfile autogenerated by cpanspec 1.78.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 1.17-1
- Specfile autogenerated by cpanspec 1.78.
