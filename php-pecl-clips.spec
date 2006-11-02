%define		_modname	clips
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - Integrated CLIPS environment for deployment of expert systems
Summary(pl):	%{_modname} - Zintegrowane ¶rodowisko CLIPS do tworzenia systemów eksperckich
Name:		php-pecl-%{_modname}
Version:	0.5.0
Release:	3
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	1c4a7fe50e16a34593256a7e6d8fe9cd
URL:		http://pecl.php.net/package/clips/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLIPS is a tool for building expert systems. This extension is an
interface to the CLIPS C library. A CLIPS environment is initialized
upon each page request. Most of the common CLIPS commands are
available as functions. Additional functions are available to create
facts and instances from associative arrays in PHP.

In PECL status of this extension is: %{_status}.

%description -l pl
CLIPS jest narzêdziem do tworzenia systemów eksperckich. Rozszerzenie
to jest interfejsem do napisanej w C biblioteki CLIPS. ¦rodowisko
CLIPS jest inicjowane z ka¿dym zapytaniem. Wiêkszo¶æ typowych poleceñ
CLIPS jest dostêpnych w postaci funkcji. Dodatkowe funkcje s± dostêpne
do tworzenia faktów i instancji z tablic asocjacyjnych PHP.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
