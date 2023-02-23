# kubescape deb rpm

[![build result](https://build.opensuse.org/projects/home:hollowman/packages/kubescape/badge.svg?type=percent)](https://build.opensuse.org/package/show/home:hollowman/kubescape)

Debian and rpm packaging scripts that allow installation of [Kubescape](https://github.com/armosec/kubescape) through the debian and rpm package manager.

## Installation

[Get the package manager repository](https://software.opensuse.org/download.html?project=home%3Ahollowman&package=kubescape) 

### Ubuntu

[Ubuntu launchpad PPA](https://launchpad.net/~hollowman86/+archive/ubuntu/kubescape)

```bash
sudo add-apt-repository ppa:hollowman86/kubescape
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
