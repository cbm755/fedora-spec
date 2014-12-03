Name:           biber
Version:        1.8
Release:        6%{?dist}
Summary:        Command-line bibliographic manager, BibTeX replacement
License:        GPL+ or Artistic
Group:          Development/Tools
URL:            http://biblatex-biber.sourceforge.net/
Source0:        https://sourceforge.net/projects/biblatex-biber/files/biblatex-biber/%{version}/biblatex-biber.tar.gz
BuildArch:      noarch

BuildRequires:  perl(autovivification)
BuildRequires:  perl(base)
BuildRequires:  perl(Business::ISBN)
BuildRequires:  perl(Business::ISSN)
BuildRequires:  perl(Business::ISMN)
BuildRequires:  perl(Config::AutoConf) >= 0.15
BuildRequires:  perl(constant)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Encode::EUCJPASCII)
BuildRequires:  perl(Encode::HanExtra)
BuildRequires:  perl(Encode::JIS2K)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.02
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(locale)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Mozilla::CA) >= 20130114
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Readonly::XS)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Storable)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::BibTeX) >= 0.66
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::GCString)
# FIXME: not available in rawhide or F21?
#BuildRequires:  perl(Unicode::Collate) >= 0.98
BuildRequires:  perl(Unicode::Collate)
BuildRequires:  perl(Unicode::Collate::Locale)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Simple)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(XML::Writer::String)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(autovivification)
Requires:       perl(Business::ISBN)
Requires:       perl(Business::ISMN)
Requires:       perl(Business::ISSN)
Requires:       perl(Data::Dump)
Requires:       perl(Data::Compare)
Requires:       perl(Date::Simple)
Requires:       perl(Encode::EUCJPASCII)
Requires:       perl(Encode::HanExtra)
Requires:       perl(Encode::JIS2K)
Requires:       perl(File::Slurp)
Requires:       perl(IPC::Cmd)
Requires:       perl(IPC::Run3)
Requires:       perl(List::AllUtils)
Requires:       perl(List::MoreUtils)
Requires:       perl(Log::Log4perl)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Mozilla::CA) >= 20130114
Requires:       perl(Regexp::Common)
Requires:       perl(Text::BibTeX) >= 0.66
# FIXME: not available in rawhide or F21?
#Requires:       perl(Unicode::Collate) >= 0.98
Requires:       perl(Unicode::Collate)
Requires:       perl(Unicode::GCString)
Requires:       perl(URI)
Requires:       perl(XML::LibXSLT)
Requires:       perl(XML::Writer)
Requires:       perl(XML::Writer::String)
# Note: biber 1.9 will need 2.9
Requires:       texlive-biblatex >= 4:svn32245.2.8a


%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.


%prep
%setup -q -n biblatex-biber-%{version}


%build
perl Build.PL
./Build


%install
./Build install --prefix %{buildroot}/usr create_packlist=0
rm -rf %{buildroot}%{_libdir}/perl5/auto %{buildroot}%{_datadir}/perl5/Unicode
chmod u+w %{buildroot}%{_bindir}/*


%files
%doc README Changes THANKS doc/%{name}.pdf
%{_bindir}/%{name}
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_datadir}/perl5/Biber*


%changelog
* Wed Dec 3 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-6
- Add Requires, taken from Build.pl.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-5
- Use sourceforge for Source0 instead of particular git commit.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.8-4
- lots more BRs, perm fixes.

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
