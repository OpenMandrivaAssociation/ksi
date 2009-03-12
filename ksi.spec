%define	name	ksi
%define	version	3.4.3
%define	release %mkrel 1

%define major	1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d


Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Implementation of the Scheme programming language
License:	BSD
Group:		Development/Other
URL:		http://ksi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ksi/%{name}-%{version}.tar.gz
BuildRequires:	readline-devel
BuildRequires:	libgc-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}
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

%package -n	%{develname}
Group:		Development/Other
License:	BSD
Summary:	Implementation of the Scheme programming language
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname %{name} -d 1

%description -n	%{develname}
KSI Scheme is an implementation of the Scheme programming language written 
in C.
It can be used as both a stand-alone interpreter and an extension library.
However, the documentation is in Russian.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall

# remove misplaced .so files
rm %{buildroot}/%{_datadir}/ksi/3.4/*.so

%multiarch_includes %{buildroot}/usr/include/ksi/ksi_path.h

%clean
rm -rf %{buildroot}

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
%{_datadir}/ksi

%files -n %{libname}
%defattr (-,root,root)
%dir %{_libdir}/ksi
%{_libdir}/ksi/*.so.*

%files -n %{develname}
%defattr (-,root,root)
%{_bindir}/ksi-config
%dir %{_includedir}/ksi
%multiarch %multiarch_includedir/ksi/*
%{_includedir}/ksi/*
%{_libdir}/ksi/*.so
%{_libdir}/ksi/*.a
%{_libdir}/ksi/*.la

