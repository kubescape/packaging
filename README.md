# kubescape Packaging
[![Version](https://img.shields.io/github/v/release/kubescape/packaging)](https://github.com/kubescape/packaging/releases)
[![Build deb or rpm packages](https://github.com/kubescape/packaging/actions/workflows/build.yml/badge.svg)](https://github.com/kubescape/packaging/actions/workflows/build.yml)
[![Release with upstream](https://github.com/kubescape/packaging/actions/workflows/release.yml/badge.svg)](https://github.com/kubescape/packaging/actions/workflows/release.yml)
[![GitHub](https://img.shields.io/github/license/kubescape/packaging)](https://github.com/kubescape/packaging/blob/master/LICENSE)
[![CNCF](https://shields.io/badge/CNCF-Sandbox%20project-blue?logo=linux-foundation&style=flat)](https://landscape.cncf.io/card-mode?project=sandbox&selected=kubescape)
[![Twitter Follow](https://img.shields.io/twitter/follow/kubescape?style=social)](https://twitter.com/kubescape)

Packaging scripts that allow installation of [Kubescape](https://github.com/armosec/kubescape) through various package manager.

## Installation
### [Ubuntu](deb/debian)
[Ubuntu launchpad PPA](https://launchpad.net/~kubescape/+archive/ubuntu/kubescape)

```bash
sudo add-apt-repository ppa:kubescape/kubescape
sudo apt update
sudo apt install kubescape
```

### [Arch Linux](PKGBUILD)
[AUR](https://aur.archlinux.org/packages/kubescape)

```bash
yay -S kubescape
```

### All kinds of package manager
[Instructions for package managers](https://software.opensuse.org/download.html?project=home%3Akubescape&package=kubescape) 

### [Snap](snap)
[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/kubescape)

```bash
sudo snap install kubescape --classic
```

### Manually
Get the latest debian or [rpm](kubescape.spec) package from the [Release Assets](https://github.com/kubescape/packaging/releases):
- `kubescape-2.2.6-0.aarch64.rpm`: Kubescape rpm package for arm64 (aarch64)
- `kubescape-2.2.6-0.x86_64.rpm`: Kubescape rpm package for amd64 (x86_64)
- `kubescape-bash-completion-2.2.6-0.noarch.rpm`: Kubescape bash auto completion rpm package
- `kubescape-fish-completion-2.2.6-0.noarch.rpm`: Kubescape fish auto completion rpm package
- `kubescape-zsh-completion-2.2.6-0.noarch.rpm`: Kubescape zsh auto completion rpm package
- `kubescape_2.2.6.dsc`: Debian Signed Kubescape source package description
- `kubescape_2.2.6.tar.xz`: Debian Kubescape vendored source package + golang compiler source package
- `kubescape_2.2.6_amd64.deb`: Kubescape rpm package for amd64 (x86_64)
- `kubescape_2.2.6_arm64.deb`: Kubescape debian package for arm64 (aarch64)

Or from the latest [GitHub Actions Workflow](https://github.com/HollowMan6/kubescape-deb-rpm/actions/workflows/build.yml) Artifacts and unzip:

- `kubescape_deb_amd64.zip`: Kubescape debian package for amd64 (x86_64)
- `kubescape_deb_arm64.zip`: Kubescape debian package for arm64 (aarch64)
- `kubescape_rpm_amd64.zip`: Kubescape rpm package for amd64 (x86_64)
- `kubescape_rpm_arm64.zip`: Kubescape rpm package for arm64 (aarch64)

Install them with:
- (Debian based) `sudo dpkg -i kubescape*.deb`
- (Redhat based) `sudo dnf install */kubescape*.rpm`
- (SUSE based) `sudo zypper install */kubescape*.rpm`
