%define		php_name	php%{?php_suffix}
%define		modname	clips
%define		status		beta
Summary:	%{modname} - Integrated CLIPS environment for deployment of expert systems
Summary(pl.UTF-8):	%{modname} - Zintegrowane środowisko CLIPS do tworzenia systemów eksperckich
Name:		%{php_name}-pecl-%{modname}
Version:	0.5.0
Release:	3
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	1c4a7fe50e16a34593256a7e6d8fe9cd
URL:		http://pecl.php.net/package/clips/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLIPS is a tool for building expert systems. This extension is an
interface to the CLIPS C library. A CLIPS environment is initialized
upon each page request. Most of the common CLIPS commands are
available as functions. Additional functions are available to create
facts and instances from associative arrays in PHP.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
CLIPS jest narzędziem do tworzenia systemów eksperckich. Rozszerzenie
to jest interfejsem do napisanej w C biblioteki CLIPS. Środowisko
CLIPS jest inicjowane z każdym zapytaniem. Większość typowych poleceń
CLIPS jest dostępnych w postaci funkcji. Dodatkowe funkcje są dostępne
do tworzenia faktów i instancji z tablic asocjacyjnych PHP.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
