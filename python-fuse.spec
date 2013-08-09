%define		module	fuse

Summary:	Python bindings for FUSE
Name:		python-%{module}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/sourceforge/fuse/fuse-python-%{version}.tar.gz
# Source0-md5:	9d9c5c2311ac04291ce822dfece108f8
URL:		http://fuse.sourceforge.net/wiki/index.php/FusePython
BuildRequires:	fuse-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Suggests:	fuse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for FUSE.

%prep
%setup -qn fuse-python-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog FAQ README*
%dir %{py_sitedir}/fuseparts
%attr(755,root,root) %{py_sitedir}/fuseparts/*.so
%{py_sitedir}/fuseparts/*.py[co]
%{py_sitedir}/*.py[co]

