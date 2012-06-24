Summary:	Console RSS reader
Summary(pl.UTF-8):   Konsolowy czytnik RSS
Name:		raggle
Version:	0.4.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.raggle.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	d6fd8e1487f53e5cf89e1bf3cf3adbfc
URL:		http://www.raggle.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Ncurses
BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raggle is a console RSS aggregator, written in Ruby. Features include
customizable keybindings, basic HTML rendering, HTTP proxy support,
OPML import/export, themes, support for various versions of RSS,
Screen support, browser auto-detection, and more. Raggle has been
tested under Linux and OpenBSD, and should work properly under other
Unix variants as well.

%description -l pl.UTF-8
Raggle to konsolowy czytnik RSS napisany w Ruby. Posiada on
modyfikowalne skróty klawiszowe, podstawowe renderowanie HTML, obsługę
HTTP proxy, importowanie i eksportowanie OPML, motywy, obsługę wielu
wersji RSS, wsparcie dla screena, automatyczną identyfikację
przeglądarki i wiele więcej. Raggle został przetestowany na Linuksie i
OpenBSD, ale powinien również działać pod innymi Uniksami.

%prep
%setup -q
find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{extras,themes},%{_mandir}/man1}

cp -a extras/web_ui $RPM_BUILD_ROOT%{_datadir}/%{name}/extras
install extras/*.rb $RPM_BUILD_ROOT%{_datadir}/%{name}/extras
install themes/*.yaml $RPM_BUILD_ROOT%{_datadir}/%{name}/themes
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/extras/*[pstb].rb
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/extras
%{_datadir}/%{name}/extras/web_ui
%{_datadir}/%{name}/extras/test_html_renderer.rb
%{_datadir}/%{name}/themes
%{_mandir}/man1/*
