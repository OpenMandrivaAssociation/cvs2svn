%define name	cvs2svn
%define version	2.1.1
%define release	%mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Other
Summary: Convert CVS repositories to Subversion or Git repositories
Url: http://cvs2svn.tigris.org/
Source0: http://cvs2svn.tigris.org/files/documents/1462/39396/%{name}-%{version}.tar.gz
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
cvs2svn is a tool for migrating a CVS repository to Subversion or Git.
It does a complete conversion; cvs2svn is not usable for keeping a
synchronised CVS and Subversion or Git repository.

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


