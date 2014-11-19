%global git_hash 848ca84

Name:		biber
Version:	1.8
Release:	3%{?dist}
Summary:	Command-line bibliographic manager, BibTeX replacement

Group:          Development/Tools
License:	GPL+ or Artistic
URL:		http://biblatex-biber.sourceforge.net/
Source0:	plk-%{name}-v%{version}-0-g%{git_hash}.zip

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
# FIXME: how to specify biblatex >= 2.8?
Requires:       texlive-biblatex >= 4:svn32245.2.8

%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.

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
* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-3
- update description and Summary

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-2
- Add dep on (probably overly) specific texlive-biblatex

* Tue Jan 14 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-1
- Bump to 1.8
- perl-File-Slurp-Unicode no longer needed
- add perl-autovivification dep

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 1.2-1
- Initial quick-and-dirty package
