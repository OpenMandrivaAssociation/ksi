%define	name	ksi
%define	version	3.4.2
%define	release %mkrel 4

%define major	1
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} %{major} -d

Version:	%{version}
Summary:	Implementation of the Scheme programming language
Name:		%{name}
Release:	%{release}
License:	BSD
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ksi-3.4.2-gcc3.4-fix.patch.bz2
URL:		http://ksi.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# maybe, but i am not sure we should add this.
#define _requires_exceptions libgc\.so*


%description
KSI Scheme is an implementation of the Scheme programming language written 
in C. 
It can be used as both a stand-alone interpreter and an extension library. 
However, the documentation is in Russian.

%package -n	%{libname}
Group:		Development/Other
License:	BSD
Summary:	Implementation of the Scheme programming language
%define _provides_exceptions libgc.*

%description -n %{libname}
KSI Scheme is an implementation of the Scheme programming language written 
in C.
It can be used as both a stand-alone interpreter and an extension library.
However, the documentation is in Russian.

%package -n	%{libname}-devel
Group:		Development/Other
License:	BSD
Summary:	Implementation of the Scheme programming language
Requires:	%{libname} = %{version}-%{release}
Provides:	libksi-devel

%description -n	%{libname}-devel
KSI Scheme is an implementation of the Scheme programming language written 
in C.
It can be used as both a stand-alone interpreter and an extension library.
However, the documentation is in Russian.

%prep
%setup -q
%patch0 -p1 -b .gcc3.4

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# remove misplaced .so files
rm $RPM_BUILD_ROOT/%{_datadir}/ksi/3.4/*.so

%multiarch_includes $RPM_BUILD_ROOT/usr/include/ksi/ksi_path.h

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info ksi-lang.info
%_install_info ksi-lang.info-1
%_install_info ksi-lang.info-2
%_install_info ksi-lang.info-3
%_install_info ksi-lang.info-4
%_install_info ksi-lang.info-5
%_install_info ksi-lang.info-6
%_install_info ksi-lang.info-7

%_install_info ksi-lib.info
%_install_info ksi-lib.info-1
%_install_info ksi-lib.info-2
%_install_info ksi-lib.info-3

%_install_info ksi.info

%preun
%_remove_install_info ksi-lang.info
%_remove_install_info ksi-lang.info-1
%_remove_install_info ksi-lang.info-2
%_remove_install_info ksi-lang.info-3
%_remove_install_info ksi-lang.info-4
%_remove_install_info ksi-lang.info-5
%_remove_install_info ksi-lang.info-6
%_remove_install_info ksi-lang.info-7
 
%_remove_install_info ksi-lib.info
%_remove_install_info ksi-lib.info-1
%_remove_install_info ksi-lib.info-2
%_remove_install_info ksi-lib.info-3
 
%_remove_install_info ksi.info

%files -n %{name}
%defattr (-,root,root)
%doc README INSTALL TODO ChangeLog
%{_bindir}/*
%exclude %{_bindir}/ksi-config
%{_infodir}/*
%dir %{_datadir}/ksi
%dir %{_datadir}/ksi/3.4
%{_datadir}/ksi/3.4/*
%dir %{_datadir}/ksi/app
%{_datadir}/ksi/app/*
%dir %{_datadir}/ksi/site
%{_datadir}/ksi/site/*

%files -n %{libname}
%defattr (-,root,root)
%dir %{_libdir}/ksi
%{_libdir}/ksi/*.so.*

%files -n %{libname}-devel
%defattr (-,root,root)
%{_bindir}/ksi-config
%dir %{_includedir}/ksi
%multiarch %multiarch_includedir/ksi/*
%{_includedir}/ksi/*
%{_libdir}/ksi/*.so
%{_libdir}/ksi/*.a
%{_libdir}/ksi/*.la

