Summary:	An extension of GTK
Name:		granite
Version:	0.2.0
Release:	0.1
License:	GPL v3
Group:		X11/Libraries
URL:		http://elementaryos.org/
#Source0:	https://launchpad.net/granite/0.x/%{version}/+download/%{name}-%{version}.tar.gz
# bzr branch lp:granite && tar -caf granite-0.2.0-bzr527.tar.bz2 --exclude-vcs granite
Source0:	%{name}-%{version}-bzr527.tar.bz2
# Source0-md5:	8ecc6754b99aff6f0c31d2313cf552ea
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	sed >= 4.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.3.14
BuildRequires:	libgee0.6-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.16.1
BuildRequires:	vala-libgee0.6
BuildRequires:	which
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.26.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens,
AppMenus, search bars, and more found in elementary apps.

%package libs
Summary:	Library for libgranite
Group:		Libraries

%description libs
Library for libgranite.

%package devel
Summary:	Header files for libgranite
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files for libgranite.

%prep
%setup -qc
mv %{name}/* .

%{__sed} -i -e '
	s,${CMAKE_INSTALL_PREFIX}/lib,${CMAKE_INSTALL_LIBDIR},
' lib/CMakeLists.txt

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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/rue
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sma

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/granite-demo
%{_iconsdir}/hicolor/*/actions/application-menu.svg
%{_iconsdir}/hicolor/*/actions/application-menu-symbolic.svg
%{_libdir}/girepository-1.0/Granite-1.0.typelib
%{_datadir}/vala/vapi/granite.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgranite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgranite.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/granite.pc
%{_libdir}/libgranite.so
%{_datadir}/gir-1.0/Granite-1.0.gir
