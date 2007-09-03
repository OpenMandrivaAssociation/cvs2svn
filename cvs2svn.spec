%define name	cvs2svn
%define version	2.0.0
%define release	%mkrel 1

Name: cvs2svn
Version: 1.5.1
Release: %mkrel 2
License: BSD
Group: Development/Other
Summary: Convert CVS repositories to Subversion repositories
Source0: http://cvs2svn.tigris.org/files/documents/1462/15996/%{name}-%{version}.tar.gz
Url: http://cvs2svn.tigris.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: locales-en
BuildRequires: subversion 
BuildRequires: subversion-tools
BuildRequires: cvs 
BuildRequires: rcs
%py_requires 
Requires: python 
Requires: subversion 
Requires: subversion-tools
Requires: cvs	
Requires: rcs
 
BuildArch: noarch 

%description
cvs2svn aims to allows you to convert a CVS repository to 
a Subversion one. This work for complete conversion, not a synchronisation
for each commit.

The software is still in beta stage, so use it to your own risk.

%prep
%setup -q

%install
make DESTDIR=%buildroot install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COMMITTERS COPYING HACKING README www/
%attr(0755,root,root) %{_bindir}/*
%{py_sitedir}/*


