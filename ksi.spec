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
%configure2_5x
make

%install
%makeinstall

%files -n %{name}
%defattr (-,root,root)
%doc README INSTALL TODO ChangeLog
%{_bindir}/*
%exclude %{_bindir}/ksi-config
%{_datadir}/ksi

%files -n %{libname}
%defattr (-,root,root)
%dir %{_libdir}/ksi
%{_libdir}/ksi/*.so.*

%files -n %{develname}
%defattr (-,root,root)
%{_bindir}/ksi-config
%dir %{_includedir}/ksi
%{_includedir}/ksi/*
%{_libdir}/ksi/*.so
%{_libdir}/ksi/*.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4.3-3mdv2011.0
+ Revision: 620041
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 3.4.3-2mdv2010.0
+ Revision: 438167
- rebuild

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.4.3-1mdv2009.1
+ Revision: 354389
- new version
- new devel policy
- rebuild for latest readline

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix '#%%define is forbidden'
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - import ksi

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Jul 02 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.4.2-3mdv2007.0
- Rebuild for new extension
- use mkrel

* Thu Mar 17 2005 Michael Scherer <misc@mandrake.org> 3.4.2-2mdk
- remove // compilation, seems broken
- multiarch tagging
- remove libgc.so provides 

* Sun Jan 23 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 3.4.2-1mdk
- 3.4.2
- fix gcc-3.4 build (P0)
- fix devel-file-in-non-devel-package
- cosmetics

* Wed Mar 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.1-4mdk
- fix DIRM
- remove explicit dependency

* Fri Jul 25 2003 Marcel Pol <mpol@gmx.net> 3.4.1-3mdk
- rebuild
- own dirs

* Mon Mar 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.4.1-2mdk
- use mklibname

* Tue Jan 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.4.1-1mdk
- 3.4.1

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.3.3-4mdk
- rebuild for new readline

* Thu Jul 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.3.3-3mdk
- split
- rebuild

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.3.3-2mdk
- rebuild

* Tue Oct 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.3.3-1mdk
- new in contribs
