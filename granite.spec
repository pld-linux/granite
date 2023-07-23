Summary:	An extension of GTK
Summary(pl.UTF-8):	Rozszerzenie GTK
Name:		granite
Version:	0.5
Release:	1
License:	GPL v3
Group:		X11/Libraries
#Source0Download: https://github.com/elementary/granite/releases
Source0:	https://github.com/elementary/granite/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	20b7a7c0ad4f000f4e4d7308db2abbf8
URL:		http://elementaryos.org/
BuildRequires:	cmake >= 2.8
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.3.14
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.23.2
BuildRequires:	vala-libgee >= 0.8
Requires(post,postun):	/sbin/ldconfig
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Obsoletes:	granite-libs < 0.1.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens,
AppMenus, search bars, and more found in elementary apps.

%description -l pl.UTF-8
Granite to rozszerzenie GTK. Dostarcza między innymi takie popularne
widżety, jak przełączniki trybów, ekrany powitalne, AppMenu, paski
wyszukiwania i inne, jakie można spotkać w aplikacjach elementary.

%package devel
Summary:	Header files for libgranite
Summary(pl.UTF-8):	Pliki nagłówkowe libgranite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for libgranite.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe libgranite.

%package -n vala-granite
Summary:	Vala API for libgranite library
Summary(pl.UTF-8):	API języka Vala do biblioteki libgranite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.23.2
Requires:	vala-libgee >= 0.8
BuildArch:	noarch

%description -n vala-granite
Vala API for libgranite library.

%description -n vala-granite -l pl.UTF-8
API języka Vala do biblioteki libgranite.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DGSETTINGS_COMPILE=OFF \
	-DICON_UPDATE=OFF \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{rue,sma}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/granite-demo
%attr(755,root,root) %{_libdir}/libgranite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgranite.so.0
%{_iconsdir}/hicolor/*/actions/application-menu.svg
%{_iconsdir}/hicolor/*/actions/application-menu-symbolic.svg
%{_libdir}/girepository-1.0/Granite-0.1.1.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/granite.pc
%{_libdir}/libgranite.so
%{_datadir}/gir-1.0/Granite-0.1.1.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi
