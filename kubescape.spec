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


%global forgeurl https://github.com/kubescape/kubescape
Name:           kubescape
Version:        2.1.3
Release:        0
Summary:        Kubescape CLI interface
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/releases/download/v%{version}/kubescape-ubuntu-latest.tar.gz
BuildArch:      x86_64

%description
Kubescape is an open-source Kubernetes security platform for your IDE, CI/CD
pipelines, and clusters. It includes risk analysis, security, compliance, and
misconfiguration scanning, saving Kubernetes users and administrators precious
time, effort, and resources.

%prep
%setup -c

%install
mkdir -p %{buildroot}%{_bindir}
mv %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Fri Feb 10 2023 Hollow Man <hollowman@opensuse.org> - 2.1.3
- Init kubescape package
