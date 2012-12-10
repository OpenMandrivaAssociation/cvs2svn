%define name	cvs2svn
%define version	2.3.0
%define release	%mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Other
Summary: Convert CVS repositories to Subversion, Git or Bazaar repositories
Url: http://cvs2svn.tigris.org/
Source0: %{name}-%{version}.tar.gz
BuildRequires: locales-en
BuildRequires: subversion
BuildRequires: subversion-tools
BuildRequires: cvs
BuildRequires: rcs
BuildRequires: python-devel
%py_requires
Requires: python
Requires: subversion
Requires: subversion-tools
Requires: cvs
Requires: rcs
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
cvs2svn is a tool for migrating a CVS repository to Subversion Git
or Bazaar. It does a complete conversion; cvs2svn is not usable for
keeping a synchronised CVS and Subversion, Git or Bazaar repository.

%prep
%setup -q

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COMMITTERS COPYING HACKING README www/
%{_bindir}/*
%{py_sitedir}/*




%changelog
* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 2.3.0-2mdv2011.0
+ Revision: 593657
- rebuild for py2.7

* Thu Aug 27 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.0-1mdv2010.0
+ Revision: 421745
- Update to new version 2.3.0
- Mention new Bazaar support in summary and description

* Fri Jan 09 2009 Jérôme Soyer <saispo@mandriva.org> 2.2.0-1mdv2009.1
+ Revision: 327437
- New upstream version

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 2.1.1-3mdv2009.1
+ Revision: 323362
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.1.1-2mdv2009.0
+ Revision: 266545
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 28 2008 Frederik Himpe <fhimpe@mandriva.org> 2.1.1-1mdv2009.0
+ Revision: 198472
- New upstream version

* Wed Mar 19 2008 Götz Waschk <waschk@mandriva.org> 2.1.0-3mdv2008.1
+ Revision: 188864
- rebuild for missing package

* Mon Feb 25 2008 Frederik Himpe <fhimpe@mandriva.org> 2.1.0-2mdv2008.1
+ Revision: 175137
- Improve description

* Mon Feb 25 2008 Frederik Himpe <fhimpe@mandriva.org> 2.1.0-1mdv2008.1
+ Revision: 174925
- New upstream version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Jérôme Soyer <saispo@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 109380
- New release

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 78820
- new version
- update to new version 2.0.0

  + Helio Chissini de Castro <helio@mandriva.com>
    - Proper instalation

* Sun Aug 12 2007 Helio Chissini de Castro <helio@mandriva.com> 1.5.1-1mdv2008.0
+ Revision: 62352
- New upstream version


* Sun Dec 10 2006 Michael Scherer <misc@mandriva.org> 1.3.1-3mdv2007.0
+ Revision: 94452
- Rebuild for new python
- run test slower, too fast on my workstation, so it may cause problem on the
  build cluster too

* Tue Oct 31 2006 Michael Scherer <misc@mandriva.org> 1.3.1-2mdv2007.1
+ Revision: 74780
- Fix BuildRequires for testing
- Enable more verbose test
- Bump release
- Fix BuildRequires, and remove python-svn as it is not needed ( not imported, test work without it )

  + Scott Karns <scottk@mandriva.org>
    - Version 1.3.1
    - Updated spec so it will build on 2006.0
    - Fixed file attributes so executables are executable by all
    - Import cvs2svn

