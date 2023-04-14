# The command line passed variable VERSION is used to set the version string
# in the metadata and in the generated zip-file. If no VERSION is passed, the
# version string in the debian control metadata is used.
#

ifndef VERSION
	VERSION = $(shell cat deb/debian/control | grep Standards-Version | cut -d' ' -f2)
endif

ifndef GIT2GO_VERSION
	GIT2GO_VERSION = $(shell cat kubescape_full.spec | grep "global git2go_version" | cut -d' ' -f3)
endif

ifndef LIBGIT2_VERSION
	LIBGIT2_VERSION = $(shell cat kubescape_full.spec | grep "global libgit2_version" | cut -d' ' -f3)
endif

ifndef RPM_SPEC
	RPM_SPEC = kubescape_full.spec
endif

ifndef PACK_GO
	PACK_GO = YES
endif

ifndef GOVERSION
	GOVERSION = 1.19.7
endif
export GOCACHE=$(PWD)/cache

clean:
	-rm -fR rpmbuild
	-rm -fR *.deb
	-rm -fR *.rpm
	-rm -fR *.src.tar.gz
	-rm -fR *.tar.xz
	-rm -fR *.dsc
	-rm -fR *.changes
	-rm -fR *.buildinfo
	-rm -fR deb/completion
	-rm -fR deb/kubescape
	-rm -fR deb/go-go*
	-rm -fR deb/golang
	-rm -fR deb/debian/kubescape*
	-rm -fR deb/debian/debhelper-build-stamp
	-rm -fR deb/debian/files
	-rm -fR deb/debian/.debhelper
	-rm -fR *.snap
	-rm -fR *.upload

prepare:
	rm -rf $(path)/kubescape
	curl --output kubescape.src.tar.gz -L https://github.com/kubescape/kubescape/archive/v$(VERSION)/kubescape-$(VERSION).tar.gz
	curl --output git2go.src.tar.gz -L https://github.com/libgit2/git2go/archive/v$(GIT2GO_VERSION)/git2go-$(GIT2GO_VERSION).tar.gz
	curl --output libgit2.src.tar.gz -L https://github.com/libgit2/libgit2/archive/v$(LIBGIT2_VERSION)/libgit2-$(LIBGIT2_VERSION).tar.gz
	cd $(path); tar -xf ../kubescape.src.tar.gz
	mv $(path)/kubescape-$(VERSION) $(path)/kubescape
	cd $(path)/kubescape; tar -xf ../../git2go.src.tar.gz; \
		rm -rf git2go; mv git2go-$(GIT2GO_VERSION) git2go
	cd $(path)/kubescape/git2go; tar -xf ../../../libgit2.src.tar.gz; \
		rm -rf libgit2; mv libgit2-$(LIBGIT2_VERSION) libgit2

prepare-go-$(GOVERSION):
	if [ "$(PACK_GO)" = "YES" ]; then \
		rm -rf $(path)/golang $(path)/go-go*; \
		curl --output go.src.tar.gz -L https://github.com/golang/go/archive/refs/tags/go$(GOVERSION).tar.gz; \
		cd $(path); tar -xf ../go.src.tar.gz; mv go-go$(GOVERSION) golang; \
	fi

vendor: clean prepare prepare-go-$(GOVERSION)
	cd $(path)/kubescape; go mod vendor; go generate -mod vendor ./...
	cd $(path)/kubescape/git2go; go mod vendor; go generate -mod vendor ./...; mv libgit2 vendor
	sed -i 's/go install /go install -mod vendor /' $(path)/kubescape/git2go/Makefile

deb-ready:
	cd $(path); dpkg-buildpackage -F -d;

deb: path:=deb
deb: vendor deb-ready

pack: path:=deb
pack: vendor
	tar -cJf kubescape_$(VERSION).tar.xz $(path)

dsc: path:=deb
dsc: vendor
	cd $(path); \
		dpkg-buildpackage -S -d;

ppa: dsc
	dput kubescape *source.changes

snap:
	snapcraft --use-lxd

rpmdir:
	mkdir -p rpmbuild/BUILD
	mkdir -p rpmbuild/RPMS
	mkdir -p rpmbuild/SOURCES
	mkdir -p rpmbuild/SPECS
	mkdir -p rpmbuild/SRPMS

rpm: rpmdir
	rpmbuild --undefine=_disable_source_fetch -ba $(RPM_SPEC) -D "_topdir $(PWD)/rpmbuild" -D 'debug_package %{nil}'
