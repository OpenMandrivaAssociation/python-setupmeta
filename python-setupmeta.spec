# Created by pyp2rpm-3.3.5
%global pypi_name setupmeta

Name:           python-%{pypi_name}
Version:        2.8.2
Release:        1
Summary:        Simplify your setup.py
Group:          Development/Python
License:        MIT
URL:            https://github.com/zsimic/setupmeta
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)

%description
Simplify your setup.py 

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE examples/direct/LICENSE.txt examples/hierarchical/LICENSE.txt setupmeta/license.py "tests/scenarios/So complex/LICENSE.md" tests/scenarios/readmes/LICENSE tests/test_license.py
%doc README.rst examples/README.rst examples/direct/README.rst examples/direct/other/README.md examples/direct/tests/README.md examples/hierarchical/README.rst examples/single/README.rst examples/via-cfg/README.md tests/scenarios/README.rst tests/scenarios/bogus/README.md tests/scenarios/complex-reqs/README.md tests/scenarios/disabled/README.md tests/scenarios/packaged/README.md tests/scenarios/readmes/README.md tests/scenarios/readmes/README.rst tests/scenarios/readmes/README1 tests/scenarios/via_req_files/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
