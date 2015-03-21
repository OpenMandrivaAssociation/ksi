%define	name	ksi
%define	version	3.9.0
%define release 2

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
BuildRequires:	gc-devel
buildrequires:	gmp-devel
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
%configure
make

%install
%makeinstall

%files -n %{name}
%doc README INSTALL TODO ChangeLog
%{_bindir}/*
%exclude %{_bindir}/ksi-config
%{_datadir}/ksi

%files -n %{libname}
%dir %{_libdir}/ksi
%{_libdir}/ksi/*.so.*

%files -n %{develname}
%{_bindir}/ksi-config
%dir %{_includedir}/ksi
%{_includedir}/ksi/*
%{_libdir}/ksi/*.so




