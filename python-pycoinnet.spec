#
# Conditional build:
%bcond_with	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define 	module	pycoinnet
Summary:	Speaking the Bitcoin Protocol
Name:		python-pycoinnet
Version:	0.01
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/richardkiss/pycoinnet/archive/%{version}.tar.gz
# Source0-md5:	512f17827323eb1ba2bfe7952829575d
URL:		https://github.com/richardkiss/pycoinnet
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel >= 3.3
BuildRequires:	python3-modules >= 3.3
%endif
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides utilities and examples for writing tools in pure Python
that speak the bitcoin protocol on the bitcoin network.

%package -n	python3-%{module}
Summary:	Speaking the Bitcoin Protocol
Version:	0.01
Release:	1
Group:		Libraries/Python
Requires:	python3 >= 3.3

%description -n python3-%{module}
It provides utilities and examples for writing tools in pure Python
that speak the bitcoin protocol on the bitcoin network.

%prep
%setup  -q -n pycoinnet-%{version}

%build
%if %{with python2}
%py_build --build-base py2
%endif
%if %{with python3}
%py3_build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg-info
%{_examplesdir}/python-%{module}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES CREDITS README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
