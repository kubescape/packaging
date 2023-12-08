#
# spec file for building package kubescape in openSUSE Build Service (OBS)
#
# Copyright (c) 2023 The Kubescape Authors
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
Version:        3.0.1
Release:        1
Summary:        CLI interface of a Kubernetes security platform
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/kubescape/%{name}
Source0:        %{name}_%{version}.tar.xz
BuildRequires:  golang
BuildRequires:  pkg-config
BuildRequires:  cmake

%description
An open-source Kubernetes security platform for your IDE, CI/CD pipelines, and clusters.
It includes risk analysis, security, compliance, and misconfiguration scanning, saving
Kubernetes users and administrators precious time, effort, and resources.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}, generated during the build.


%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       zsh-completion
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}, generated during the build.


%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       fish-completion
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}, generated during the build.

%prep
%setup -q -n deb

%build
export GOVERSION_MAJOR=$(go version | cut -f1 -d. | cut -f4 -do)
export GOVERSION_MINOR=$(go version | cut -f2 -d. | cut -f1 -d' ')
# Use our go compiler if golang version is less than 1.19
if [[ ${GOVERSION_MAJOR} -lt 1 || ${GOVERSION_MINOR} -lt 19 ]]; then
  export GOROOT=$(pwd)/golang
  export PATH=${GOROOT}/bin:$PATH
  cd golang/src; bash ./make.bash; cd ../..
fi
export CGO_ENABLED=1
cd %{name}/git2go; make install-static; cd ..
cp -r git2go/static-build vendor/github.com/libgit2/git2go/v*/
go version
go build -mod=vendor -buildmode=pie -buildvcs=false -ldflags="-s -w -X github.com/kubescape/%{name}/v2/core/cautils.BuildNumber=v%{version}" -tags=static,gitenabled -o %{name}

%install
install -Dpm 0755 %{name}/%{name} %{buildroot}%{_bindir}/%{name}

# Bash autocomplete file
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.sh
install -Dm 644 %{name}-autocomplete.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# Zsh autocomplete file
%{buildroot}/%{_bindir}/%{name} completion zsh > %{name}-autocomplete.sh
install -Dm 644 %{name}-autocomplete.sh %{buildroot}%{_datadir}/zsh/vendor-completions/_%{name}

# Fish autocomplete file
%{buildroot}/%{_bindir}/%{name} completion fish > %{name}-autocomplete.sh
install -Dm 644 %{name}-autocomplete.sh %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%check
if [ "$(%{buildroot}%{_bindir}/%{name} version)" != "Your current version is: v%{version} [git enabled in build: true]" ]; then exit 1; fi

%files
%license %{name}/LICENSE
%doc %{name}/README.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%files fish-completion
%{_datadir}/fish

%changelog
* Thu Dec 07 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 3.0.1
- Update to 3.0.1

* Sun Aug 13 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.9.0
- Update to 2.9.0

* Tue Jul 25 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.8
- Update to 2.3.8

* Thu Jul 06 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.7
- Update to 2.3.7

* Thu Jun 15 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.6
- Update to 2.3.6

* Sun Jun 04 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.5
- Update to 2.3.5

* Sun May 28 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.4
- Update to 2.3.4

* Tue May 16 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.3
- Update to 2.3.3

* Mon May 15 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.2
- Update to 2.3.2

* Tue May 09 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.3.1
- Update to 2.3.1

* Mon Apr 03 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.6
- Update to 2.2.6

* Fri Mar 24 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.5
- Update to 2.2.5

* Sat Mar 11 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.4
- Update to 2.2.4

* Sun Feb 26 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.2
- Upgrade with patches

* Thu Feb 23 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.1
- Upgrade

* Wed Feb 15 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.2.0
- New control statuses (https://github.com/kubescape/kubescape/pull/1016)

* Fri Feb 10 2023 Kubescape Maintainers <cncf-kubescape-maintainers@lists.cncf.io> - 2.1.3
- Init kubescape package
