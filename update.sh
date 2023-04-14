git clone https://github.com/kubescape/kubescape.git --no-checkout
cd kubescape
VLATEST=$(git describe --tags --abbrev=0)
cd ..
rm -rf kubescape
export LATEST=${VLATEST:1}
export RELEASE=$(cat kubescape_full.spec | grep "Release:" | tr -s ' ' | cut -d' ' -f2)
export CURRENT=$(cat kubescape_full.spec | grep "Version:" | tr -s ' ' | cut -d' ' -f2)
UBUNTU="jammy"
if [ "$LATEST" != "$CURRENT" ]; then
    echo "New version available: $LATEST"
    curl --progress-bar -L https://github.com/kubescape/kubescape/archive/v${LATEST}/kubescape-${LATEST}.tar.gz -o kubescape-${LATEST}.tar.gz
    export CURRENTSHA512=$(cat PKGBUILD | grep "sha512sums=(" | cut -d\' -f2)
    export NEWSHA512=$(sha512sum kubescape-${LATEST}.tar.gz |  cut -d' ' -f1)
    rm kubescape-${LATEST}.tar.gz
    sed -i "s/$CURRENTSHA512/$NEWSHA512/g" PKGBUILD
    sed -i "s/pkgver=$CURRENT/pkgver=$LATEST/g" PKGBUILD*
    sed -i "s/Version:        $CURRENT/Version:        $LATEST/g" kubescape*.spec
    sed -i "s/Release:.*/Release:        0/g" kubescape*.spec
    sed -i "s/%changelog/%changelog\n* $(date +"%a %b %d %Y") github-actions[bot] <github-actions[bot]@users.noreply.github.com> - $LATEST\n- Update to $LATEST\n/g" kubescape*.spec
    sed -i "s/Standards-Version: $CURRENT/Standards-Version: $LATEST/g" deb/debian/control
    sed -i "1s/^/kubescape ($LATEST) $UBUNTU; urgency=medium\n\n  * v$LATEST: Update\n\n -- Hollow Man <hollowman@opensuse.org>  $(date +"%a, %d %b %Y %H:%M:%S %z")\n\n/" deb/debian/changelog
    sed -i "s/version: '$CURRENT'/version: '$LATEST'/g" snap/snapcraft.yaml
else
    echo "No new version available"
    sed -i "s/pkgrel=${RELEASE}/pkgrel=$((RELEASE+1))/g" PKGBUILD*
    sed -i "s/Release:.*/Release:        $((RELEASE+1))/g" kubescape*.spec
fi
