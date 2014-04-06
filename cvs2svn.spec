Name:		cvs2svn
Version:	2.4.0
Release:	1
License:	BSD
Group:		Development/Other
Summary:	Convert CVS repositories to Subversion, Git or Bazaar repositories
Url:		http://cvs2svn.tigris.org/
Source0:	http://cvs2svn.tigris.org/files/documents/1462/49237/%{name}-%{version}.tar.gz
BuildRequires:	locales-en
BuildRequires:	subversion
BuildRequires:	subversion-tools
BuildRequires:	cvs
BuildRequires:	git
BuildRequires:	rcs
BuildRequires:	pkgconfig(python2)
Requires:	subversion
Requires:	subversion-tools
Requires:	cvs
Requires:	git
Requires:	rcs
BuildArch:	noarch

%description
cvs2svn is a tool for migrating a CVS repository to Subversion Git
or Bazaar. It does a complete conversion; cvs2svn is not usable for
keeping a synchronised CVS and Subversion, Git or Bazaar repository.

%prep
%setup -q

%build
python setup.py build

%install
%makeinstall_std

%files
%doc BUGS COMMITTERS COPYING HACKING README www/
%{_bindir}/*
%{py_sitedir}/*
