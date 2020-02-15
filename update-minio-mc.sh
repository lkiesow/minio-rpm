#!/bin/sh

echo "Checking minio-mc"

LATEST="$(
	curl -s 'https://github.com/minio/mc/releases' \
		| sed -n 's_^.*href="/minio/mc/tree/\(RELEASE\.[^"]*\)".*$_\1_p' \
		| head -n1
	)"

echo "Latest version:  $LATEST"

PKG="$(
	cat minio-mc.spec \
		| grep '%define *tag' \
		| awk '{print $3}'
	)"

echo "Package version: $PKG"

if [ "$LATEST" != "$PKG" ]; then
	DATE="$(date "+%a %b %d %Y")"
	USER="Lars Kiesow <lkiesow@uos.de>"
	VERSION="0.1.$(echo "${LATEST}" | tr -d '-')-1"
	sed -i "s/^%define  tag .*/%define  tag   ${LATEST}/" minio-mc.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${VERSION}\n- Update to ${LATEST}\n/" minio-mc.spec
fi
