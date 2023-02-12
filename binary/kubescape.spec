#
# spec file for package kubescape
#
# Copyright (c) 2023 Hollow Man
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/kubescape/kubescape/issues
#


Name:           kubescape
Version:        2.1.3
Release:        0
Summary:        Kubescape CLI interface
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/kubescape/kubescape
Source0:        kubescape_%{version}.tar.xz
Provides:       %{name} = %{version}

%description
Kubescape is an open-source Kubernetes security platform for your IDE, CI/CD
pipelines, and clusters. It includes risk analysis, security, compliance, and
misconfiguration scanning, saving Kubernetes users and administrators precious
time, effort, and resources.

%prep
%setup -q -n binary

%build
mv %{name}/$(uname -m)/%{name} %{name}/

%install
install -Dpm 0755 %{name}/%{name} %{buildroot}%{_bindir}/%{name}

%check
if [ "$(%{buildroot}%{_bindir}/%{name} version)" != "Your current version is: v%{version} [git enabled in build: true]" ]; then exit 1; fi

%files
%{_bindir}/%{name}

%changelog
* Fri Feb 10 2023 Hollow Man <hollowman@opensuse.org> - 2.1.3
- Init kubescape package
