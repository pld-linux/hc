Summary:	Hanzi Converter between BIG-5 and GB codes
Summary(pl.UTF-8):	Konwerter kodowania ideogramów chińskich (Hanzi) w BIG-5 i GB
Name:		hc
Version:	3.0
Release:	2
License:	non-commercial use and distribution
Group:		Applications/Text
Source0:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/hc-30.tar.gz
# Source0-md5:	e3a0fad6154e1d3f4e8abbb52abf28e1
Source1:	ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/hc-supp.tab
# Source1-md5:	5b12db3fbe75b4b252a4f588a1d25a58
Patch0:		hc-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is version 3.0 of Hanzi Converter, which converts between GB and
BIG-5 codes. The conversion table has been revised with corrections.
This version supports more options, including the showing of all
multiple mappings, please see the man page for more detail.

%description -l pl.UTF-8
Jest to wersja 3.0 konwertera pomiędzy kodowaniami ideogramów chińskich
(Hanzi) w GB i BIG-5. Tabela konwersji została przejrzana i poprawiona.
Niniejsza wersja zawiera wsparcie dla większej liczby opcji, w tym
dla pokazywania wszystkich możliwych przekodowań. Szczegóły opisano na
stronie podręcznika man.

%prep
%setup -q -n hc3
install %{SOURCE1} .
%patch -P0 -p1

%build
%{__make}
%{__make} b2g g2b

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/chinese,%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install hc b2g g2b	$RPM_BUILD_ROOT%{_bindir}
install hc.1		$RPM_BUILD_ROOT%{_mandir}/man1
install hc*.tab		$RPM_BUILD_ROOT%{_datadir}/chinese
install poem.*		$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/chinese
%config %{_datadir}/chinese/hc.tab
%config %{_datadir}/chinese/hc-supp.tab
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}
