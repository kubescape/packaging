# The command line passed variable VERSION is used to set the version string
# in the metadata and in the generated zip-file. If no VERSION is passed, the
# version string in the debian control metadata is used.
#

ifndef VERSION
	VERSION = $(shell cat deb/debian/control | grep Standards-Version | cut -d' ' -f2)
endif

clean:
	-rm -fR deb/_build
	-rm -fR rpmbuild
	-rm -fR *.deb
	-rm -fR *.rpm
	-rm -fR *.tar.gz
	-rm -fR *.tar.xz
	-rm -fR *.dsc
	-rm -fR *.changes
	-rm -fR *.buildinfo
	-rm -fR deb/LISENCE
	-rm -fR deb/kubescape
	-rm -fR deb/debian/kubescape*
	-rm -fR deb/debian/debhelper-build-stamp
	-rm -fR deb/debian/files
	-rm -fR deb/debian/.debhelper
	-rm -fR *.upload

debprepare:
	curl --output src.tar.gz -L https://github.com/kubescape/kubescape/releases/download/v$(VERSION)/kubescape-ubuntu-latest.tar.gz
	mkdir -p deb/_build
	cd deb/_build; tar -xf ../../src.tar.gz; rm LICENSE
	rm -f src.tar.gz

deb: debprepare
	cd deb; dpkg-buildpackage -F

ppa: clean debprepare
	cd deb; \
		dpkg-buildpackage -S;
	dput $(NAME) *source.changes

rpm:
	mkdir -p rpmbuild/BUILD
	mkdir -p rpmbuild/RPMS
	mkdir -p rpmbuild/SOURCES
	mkdir -p rpmbuild/SPECS
	mkdir -p rpmbuild/SRPMS
	rpmbuild --undefine=_disable_source_fetch -ba kubescape.spec -D "_topdir $(PWD)/rpmbuild"
