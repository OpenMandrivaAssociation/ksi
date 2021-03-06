%define	name	ksi
%define	version	3.9.0
%define release 4

%define major	1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
#self provided req.
%define __noautoreq '/usr/bin/ksi'
%define _disable_rebuild_configure 1

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Implementation of the Scheme programming language
License:	BSD
Group:		Development/Other
URL:		http://ksi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ksi/%{name}-%{version}.tar.gz
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	gmp-devel

%description
KSI Scheme is an implementation of the Scheme programming language written 
in C. 
It can be used as both a stand-alone interpreter and an extension library. 
However, the documentation is in Russian.

%files -n %{name}
%doc README TODO ChangeLog
%{_bindir}/*
%exclude %{_bindir}/ksi-config
%{_datadir}/ksi
#--------------------------------------------

%package -n	%{libname}
Group:		Development/Other
License:	BSD
Summary:	Implementation of the Scheme programming language

%description -n %{libname}
KSI Scheme is an implementation of the Scheme programming language written 
in C.
It can be used as both a stand-alone interpreter and an extension library.
However, the documentation is in Russian.

%files -n %{libname}
%doc README TODO ChangeLog
%dir %{_libdir}/ksi
%{_libdir}/ksi/*.so.*
#--------------------------------------------
%package -n	%{develname}
Group:		Development/Other
License:	BSD
Summary:	Implementation of the Scheme programming language
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{develname} < %{EVRD}

%description -n	%{develname}
KSI Scheme is an implementation of the Scheme programming language written 
in C.
It can be used as both a stand-alone interpreter and an extension library.
However, the documentation is in Russian.


%files -n %{develname}
%doc README TODO ChangeLog
%{_bindir}/ksi-config
%dir %{_includedir}/ksi
%{_includedir}/ksi/*
%{_libdir}/ksi/*.so
#--------------------------------------------


%prep
%setup -q
autoreconf -fiv

%build
%configure
make -v

%install
%makeinstall






