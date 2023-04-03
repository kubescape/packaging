# kubescape Packaging

[![build result](https://build.opensuse.org/projects/home:kubescape/packages/kubescape/badge.svg?type=percent)](https://build.opensuse.org/package/show/home:kubescape/kubescape)

Packaging scripts that allow installation of [Kubescape](https://github.com/armosec/kubescape) through various package manager.

## Installation

[Get the package manager repository](https://software.opensuse.org/download.html?project=home%3Akubescape&package=kubescape) 

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/cli-kubescape)

### Snap
> Note: If installed using snap, the following limitations apply:
> - The executable is called `cli-kubescape` and not `kubescape`.
> - Kubenetes cluster scan is not supported.

```bash
sudo snap install cli-kubescape
```

### Ubuntu

[Ubuntu launchpad PPA](https://launchpad.net/~kubescape/+archive/ubuntu/kubescape)

```bash
sudo add-apt-repository ppa:kubescape/kubescape
sudo apt update
sudo apt install kubescape
```

### Manually
Get the latest debian or rpm package from the [GitHub Actions Workflow](https://github.com/HollowMan6/kubescape-deb-rpm/actions/workflows/build.yml) Artifacts.

- `kubescape_deb_amd64.zip`: Kubescape debian package for amd64 (x86_64)
- `kubescape_deb_arm64.zip`: Kubescape debian package for arm64 (aarch64)
- `kubescape_rpm_amd64.zip`: Kubescape rpm package for amd64 (x86_64)
- `kubescape_rpm_arm64.zip`: Kubescape rpm package for arm64 (aarch64)

Unzip the package and install it with:
- (Debian based) `sudo dpkg -i kubescape*.deb`
- (Redhat based) `sudo dnf install */kubescape*.rpm`
- (SUSE based) `sudo zypper install */kubescape*.rpm`.
