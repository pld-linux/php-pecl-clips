%define		_modname	clips
%define		_status		beta

Summary:	%{_modname} - Integrated CLIPS environment for deployment of expert systems
Summary(pl):	%{_modname} - Zintegrowane ¶rodowisko CLIPS do tworzenia systemów eksperckich
Name:		php-pecl-%{_modname}
Version:	0.5.0
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	1c4a7fe50e16a34593256a7e6d8fe9cd
URL:		http://pecl.php.net/package/clips/
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

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
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
