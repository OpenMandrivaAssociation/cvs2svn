%define name	cvs2svn
%define version	2.1.0
%define release	%mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
License: BSD
Group: Development/Other
Summary: Convert CVS repositories to Subversion repositories
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
cvs2svn aims to allows you to convert a CVS repository to
a Subversion one. This work for complete conversion, not a synchronisation
for each commit.

The software is still in beta stage, so use it to your own risk.

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


