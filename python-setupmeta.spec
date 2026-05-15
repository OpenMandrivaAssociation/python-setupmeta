%define module setupmeta
%bcond tests 1

Name:		python-setupmeta
Version:	3.9.0
Release:	1
Summary:	Simplify your setup.py
Group:		Development/Python
License:	MIT
URL:		https://github.com/codrsquad/setupmeta
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	git-core
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(mock)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%endif


%description
Writing a setup.py typically involves lots of boilerplate and copy-pasting
from project to project.

This package aims to simplify that and bring some DRY principle to python
packaging.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
# to avoid a self dependency bootstrap loop, we build the wheel twice
# 1) this generates a wheel with version 0.0.0
%py_build
# 2) we use it to generate the versioned wheel
export PYTHONPATH=RPMBUILD_wheels/setupmeta-0.0.0-py3-none-any.whl
%py_build_wheel
# remove the first wheel
rm -rf RPMBUILD_wheels/setupmeta-0.0.0-py3-none-any.whl

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# required for some tests
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# test_check_dependencies: requires a virtualenv
# test_version and test_scenario require full git project with its versioning scheme, disabled
pytest tests/ -k "not test_check_dependencies and not test_scenario and not test_commands and not test_requirements"
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
