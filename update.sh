git clone https://github.com/kubescape/kubescape.git --no-checkout
cd kubescape
VLATEST=$(git describe --tags --abbrev=0)
cd ..
rm -rf kubescape
export LATEST=${VLATEST:1}
export RELEASE=$(cat kubescape.spec | grep "Release:" | tr -s ' ' | cut -d' ' -f2)
CURRENT=$(cat kubescape.spec | grep "Version:" | tr -s ' ' | cut -d' ' -f2)
UBUNTU="kinetic"
if [ "$LATEST" != "$CURRENT" ]; then
    echo "New version available: $LATEST"
    sed -i "s/Version:        $CURRENT/Version:        $LATEST/g" kubescape*.spec
    sed -i "s/Release:.*/Release:        0/g" kubescape*.spec
    sed -i "s/%changelog/%changelog\n* $(date +"%a %b %d %Y") github-actions[bot] <github-actions[bot]@users.noreply.github.com> - $LATEST\n- Update to $LATEST\n/g" kubescape*.spec
    sed -i "s/Standards-Version: $CURRENT/Standards-Version: $LATEST/g" deb/debian/control
    sed -i "1s/^/kubescape ($LATEST) $UBUNTU; urgency=medium\n\n  * v$LATEST: Update\n\n -- github-actions[bot] <github-actions[bot]@users.noreply.github.com>  $(date +"%a, %d %b %Y %H:%M:%S %z")\n\n/" deb/debian/changelog
else
    echo "No new version available"
    sed -i "s/Release:.*/Release:        $((RELEASE+1))/g" kubescape*.spec
fi
