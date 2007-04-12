%define name	cvs2svn
%define version	1.3.1
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Development/Other
Summary:	Convert CVS repositories to Subversion repositories
Source0:        http://cvs2svn.tigris.org/files/documents/1462/15996/%{name}-%{version}.tar.bz2
Url:		http://cvs2svn.tigris.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# for testing 
BuildRequires: locales-en
BuildRequires: python 
BuildRequires: subversion subversion-tools
BuildRequires: cvs rcs
Requires:	python 
Requires:	subversion subversion-tools
Requires:	cvs	rcs
 
BuildArch:	noarch 

%description
cvs2svn aims to allows you to convert a CVS repository to 
a Subversion one. This work for complete conversion, not a synchronisation
for each commit.

The software is still in beta stage, so use it to your own risk.

%prep
%setup -q

%build

%check
# needed for testing
LANG=en_US.UTF-8
export LANG
unset LANGUAGE LC_MESSAGES
# better error reporting in case of problem
# running without nice make test fails, on os.wait()
# because my computer is too fast ( amd 64 2 ghz ) 
nice -n 10 ./run-tests.py -v

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}/
cp %name verify-cvs2svn %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{py_sitedir}/
cp -r cvs2svn_rcsparse %{buildroot}/%{py_sitedir}/

mkdir -p %{buildroot}/%{_mandir}/man1
cp %{name}.1 %{buildroot}/%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COMMITTERS COPYING HACKING README www/
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{py_sitedir}/cvs2svn_rcsparse


