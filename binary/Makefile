# The command line passed variable VERSION is used to set the version string
# in the metadata and in the generated zip-file. If no VERSION is passed, the
# version string in the debian control metadata is used.
#

ifndef VERSION
	VERSION = $(shell cat ../kubescape.spec | grep Version: | tr -s ' ' | cut -d' ' -f2)
endif

ifndef GIT2GO_VERSION
	GIT2GO_VERSION = $(shell cat ../kubescape.spec | grep "global git2go_version" | cut -d' ' -f3)
endif

ifndef LIBGIT2_VERSION
	LIBGIT2_VERSION = $(shell cat ../kubescape.spec | grep "global libgit2_version" | cut -d' ' -f3)
endif

export CGO_ENABLED=1
export GOCACHE=$(PWD)/../cache

ARCH = $(shell uname -m)
BUILDCMD = go build -buildmode=pie -buildvcs=false -ldflags="-s -w -X github.com/kubescape/kubescape/v2/core/cautils.BuildNumber=v$(VERSION)" -tags=static,gitenabled -o

clean:
	-rm -fR rpmbuild
	-rm -fR *.deb
	-rm -fR *.rpm
	-rm -fR *.src.tar.gz
	-rm -fR *.tar.xz
	-rm -fR *.dsc
	-rm -fR *.changes
	-rm -fR *.buildinfo
	-rm -fR LISENCE
	-rm -fR debian/debhelper-build-stamp
	-rm -fR debian/files
	-rm -fR debian/.debhelper
	-rm -fR *.upload

clean-all: clean
	-rm -fR kubescape
	-rm -fR debian/source
	-rm -fR debian/tests
	-rm -fR debian/changelog
	-rm -fR debian/compat
	-rm -fR debian/control
	-rm -fR debian/copyright
	-rm -fR debian/install

clean-build:
	cd kubescape; tar -xf ../git2go.src.tar.gz; \
		rm -rf git2go; mv git2go-$(GIT2GO_VERSION) git2go
	cd kubescape/git2go/vendor; tar -xf ../../../libgit2.src.tar.gz; \
		rm -rf libgit2; mv libgit2-$(LIBGIT2_VERSION) libgit2

prepare:
	rm -rf kubescape
	curl --output kubescape.src.tar.gz -L https://github.com/kubescape/kubescape/archive/v$(VERSION)/kubescape-$(VERSION).tar.gz
	curl --output git2go.src.tar.gz -L https://github.com/libgit2/git2go/archive/v$(GIT2GO_VERSION)/git2go-$(GIT2GO_VERSION).tar.gz
	curl --output libgit2.src.tar.gz -L https://github.com/libgit2/libgit2/archive/v$(LIBGIT2_VERSION)/libgit2-$(LIBGIT2_VERSION).tar.gz
	tar -xf kubescape.src.tar.gz
	mv kubescape-$(VERSION) kubescape

binary: clean-build
	cd kubescape/git2go; make install-static;
	cd kubescape; $(BUILDCMD) bin/$(ARCH)/kubescape;

deb:
	cp -nr ../deb/debian/* debian
	cp -r kubescape/bin .
	sudo rm -rf kubescape
	mv bin kubescape
	sed -i "s/ golang, cmake, pkg-config, / /g" debian/control
	dpkg-buildpackage -S
