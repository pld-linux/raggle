%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Console RSS reader
Summary(pl):	Konsolowy czytnik RSS
Name:		raggle
Version:	0.3.1
Release:	2
License:	GPL
Group:		Applications
Source0:	http://www.raggle.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	6d700fefe3ec875b6cdf504afa12bbe5
URL:		http://www.raggle.org/
BuildRequires:	ruby
Requires:	ruby-Ncurses
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raggle is a console RSS aggregator, written in Ruby. Features include
customizable keybindings, basic HTML rendering, HTTP proxy support,
OPML import/export, themes, support for various versions of RSS,
Screen support, browser auto-detection, and more. Raggle has been
tested under Linux and OpenBSD, and should work properly under other
Unix variants as well.

%description -l pl
Raggle to konsolowy czytnik RSS napisany w Ruby. Posiada on
modyfikowalne skróty klawiszowe, podstawowe renderowanie HTML, obs³ugê
HTTP proxy, importowanie i eksportowanie OPML, motywy, obs³ugê wielu
wersji RSS, wsparcie dla screena, automatyczn± identyfikacjê
przegl±darki i wiele wiêcej. Raggle zosta³ przetestowany na Linuksie i
OpenBSD, ale powinien równie¿ dzia³aæ pod innymi Uniksami.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

cp -a themes extras $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*
