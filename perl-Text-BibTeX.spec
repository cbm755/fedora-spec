Name:           perl-Text-BibTeX
Version:        0.69
Release:        1%{?dist}
Summary:        Interface to read and parse BibTeX files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-BibTeX/
Source0:        http://www.cpan.org/authors/id/A/AM/AMBS/Text/Text-BibTeX-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(Config::AutoConf) >= 0.16
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Simple)
BuildRequires:  chrpath
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Text::BibTeX module serves mainly as a high-level introduction to the
Text::BibTeX library, for both code and documentation purposes. The code
loads the two fundamental modules for processing BibTeX files
(Text::BibTeX::File and Text::BibTeX::Entry), and this documentation gives
a broad overview of the whole library that isn't available in the
documentation for the individual modules that comprise it.

%prep
%setup -q -n Text-BibTeX-%{version}
sed -i 's#/usr/local/bin/perl5#/usr/bin/perl#' scripts/* examples/*
sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' scripts/*

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT


# TODO: stuff in btparse should be installed somewhere?  Or is it really docs?
%files
%defattr(-,root,root,-)
%doc btparse Changes examples META.json README README.OLD scripts THANKS xscode
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so

%changelog
* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 0.69-1
- Changes file changed case.
- Add a TODO for the various files doc files.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 0.64-1
- Specfile autogenerated by cpanspec 1.78.