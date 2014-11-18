%global git_hash d9d65aa
#(for 1.9 it was 65e3cef)
#(for 1.8 it was 848ca84)

Name:		biber
Version:	1.9
Release:	3%{?dist}
Summary:	A BibTeX replacement for users of BibLaTeX

Group:          Development/Tools
License:	GPL+ or Artistic
URL:		http://biblatex-biber.sourceforge.net/
# https://github.com/plk/biber/zipball/v1.8
# for 1.9, didn't use a tag b/c want one commit after the tag
Source0:	plk-%{name}-v%{version}-2-g%{git_hash}.zip

BuildArch:      noarch

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Config::AutoConf)
BuildRequires:	perl(ExtUtils::LibBuilder)

Requires:	perl(Data::Dump)
Requires:       perl(Data::Compare)
Requires:       perl(Date::Simple)
Requires:       perl(File::Slurp)
Requires:       perl(IPC::Cmd)
Requires:       perl(IPC::Run3)
Requires:       perl(List::AllUtils)
Requires:       perl(List::MoreUtils)
Requires:       perl(Regexp::Common)
Requires:       perl(Log::Log4perl)
Requires:       perl(Unicode::Collate)
Requires:       perl(XML::LibXML::Simple)
Requires:       perl(XML::LibXSLT)
Requires:       perl(XML::Writer::String)
Requires:       perl(Text::BibTeX)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Business::ISBN)
Requires:       perl(Business::ISSN)
Requires:       perl(Business::ISMN)
Requires:       perl(Mozilla::CA)
Requires:       perl(Readonly::XS)
Requires:       perl(autovivification)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The biblatex package by Philipp Lehman is becoming the definitive citation
management tool for LaTeX users. Biblatex has relied on the venerable
BibTeX program only for sorting and generating a very generic .bbl file
without any formatting instruction. Everything else is taken care of by
biblatex, which provides a powerful and flexible macro interface for
authors of citation styles.

%prep
%setup -q -n plk-%{name}-%{git_hash}


%build
perl Build.PL
./Build


%install
./Build install --prefix %{buildroot}/usr
rm -rf %{buildroot}%{_libdir}/perl5/auto %{buildroot}%{_datadir}/perl5/Unicode


%files
%doc README Changes THANKS doc/%{name}.pdf
%{_bindir}/%{name}
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_datadir}/perl5/Biber*



%changelog
* Tue Nov 18 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.9-3
- rev bump to try to fix copr for F21

* Fri Jun 27 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.9-1
- Bump to 1.9 (actually one commit past the tag for 1.9)

* Tue Jan 14 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-1
- Bump to 1.8
- perl-File-Slurp-Unicode no longer needed
- add perl-autovivification dep

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 1.2-1
- Initial quick-and-dirty package
