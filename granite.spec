Summary:	An extension of GTK
Name:		granite
Version:	0.1.1
Release:	1
License:	GPL v3
Group:		X11/Libraries
URL:		http://elementaryos.org/
Source0:	https://launchpad.net/granite/0.x/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	c25c4bd409a1dbe2e5fc99c305e1dc36
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libgee0.6-devel
BuildRequires:	libstdc++-devel
BuildRequires:	vala
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens,
AppMenus, search bars, and more found in elementary apps.

%package devel
Summary:	Header files for libgranite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens,
AppMenus, search bars, and more found in elementary apps.

This package contains the header files

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/granite-demo
%attr(755,root,root) %{_libdir}/libgranite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgranite.so.0
%{_iconsdir}/hicolor/*/actions/application-menu.svg
%{_iconsdir}/hicolor/*/actions/application-menu-symbolic.svg
%{_libdir}/girepository-1.0/Granite-0.1.1.typelib
%{_datadir}/vala/vapi/granite.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/granite.pc
%{_libdir}/libgranite.so
%{_datadir}/gir-1.0/Granite-0.1.1.gir
