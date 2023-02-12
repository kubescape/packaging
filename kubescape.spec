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


%global git2go_version 33.0.9
%global libgit2_version 1.3.0
Name:           kubescape
Version:        2.1.3
Release:        0
Summary:        Kubescape CLI interface
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/kubescape/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/libgit2/git2go/archive/v%{git2go_version}/git2go-%{git2go_version}.tar.gz
Source2:        https://github.com/libgit2/libgit2/archive/v%{libgit2_version}/libgit2-%{libgit2_version}.tar.gz
BuildRequires:  golang
BuildRequires:  pkg-config
BuildRequires:  cmake
Provides:       %{name} = %{version}

%description
Kubescape is an open-source Kubernetes security platform for your IDE, CI/CD
pipelines, and clusters. It includes risk analysis, security, compliance, and
misconfiguration scanning, saving Kubernetes users and administrators precious
time, effort, and resources.

%prep
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1
%setup -q -T -D -a 2
rm -rf git2go && mv git2go-%{git2go_version} git2go
rm -rf git2go/vendor/libgit2 && mv libgit2-%{libgit2_version} git2go/vendor/libgit2

%build
export CGO_ENABLED=1
export GOCACHE=${PWD}/../../../cache
cd git2go && make install-static && cd ..
go build -buildmode=pie -buildvcs=false -ldflags="-s -w -X github.com/kubescape/%{name}/v2/core/cautils.BuildNumber=v%{version}" -tags=static,gitenabled -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
if [ "$(%{buildroot}%{_bindir}/%{name} version)" != "Your current version is: v%{version} [git enabled in build: true]" ]; then exit 1; fi

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Feb 10 2023 Hollow Man <hollowman@opensuse.org> - 2.1.3
- Init kubescape package
