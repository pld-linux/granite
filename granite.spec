Summary:	An extension of GTK
Summary(pl.UTF-8):	Rozszerzenie GTK
Name:		granite
Version:	6.2.0
Release:	1
License:	GPL v3
Group:		X11/Libraries
#Source0Download: https://github.com/elementary/granite/releases
Source0:	https://github.com/elementary/granite/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b5cb2159d784020667c87d21f82157c1
URL:		http://elementaryos.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	meson >= 0.48.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	vala >= 2:0.48
BuildRequires:	vala-libgee >= 0.8
Requires(post,postun):	/sbin/ldconfig
Requires:	glib2 >= 1:2.50
Requires:	gtk+3 >= 3.22
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
Requires:	glib2-devel >= 1:2.50
Requires:	gtk+3-devel >= 3.22

%description devel
This package contains the header files for libgranite.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe libgranite.

%package -n vala-granite
Summary:	Vala API for libgranite library
Summary(pl.UTF-8):	API języka Vala do biblioteki libgranite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.48
Requires:	vala-libgee >= 0.8
BuildArch:	noarch

%description -n vala-granite
Vala API for libgranite library.

%description -n vala-granite -l pl.UTF-8
API języka Vala do biblioteki libgranite.

%prep
%setup -q

%build
%meson build \
	--default-library=shared \
	-Ddocumentation=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,rue,sma}

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
%doc README.md
%attr(755,root,root) %{_bindir}/granite-demo
%attr(755,root,root) %{_libdir}/libgranite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgranite.so.6
%{_libdir}/girepository-1.0/Granite-1.0.typelib
%{_datadir}/metainfo/granite.appdata.xml
%{_desktopdir}/io.elementary.granite.demo.desktop
%{_iconsdir}/hicolor/*x*/actions/appointment.svg
%{_iconsdir}/hicolor/*x*/actions/open-menu.svg
%{_iconsdir}/hicolor/scalable/actions/open-menu-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgranite.so
%{_includedir}/granite
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_pkgconfigdir}/granite.pc

%files -n vala-granite
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi
