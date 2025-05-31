#!/bin/bash

set -e

APP_NAME="iframextract"
VERSION="1.0.0"
ARCH="all"
PKG_NAME="${APP_NAME}_${VERSION}_${ARCH}"
BUILD_DIR="./dist/${PKG_NAME}"
BIN_DIR="${BUILD_DIR}/usr/bin"
CONTROL_FILE="${BUILD_DIR}/DEBIAN/control"

# Clean previous builds
rm -rf dist
mkdir -p "${BIN_DIR}"
mkdir -p "$(dirname "${CONTROL_FILE}")"

# Create CLI launcher
echo "#!/bin/bash
exec python3 -m iframextract.cli \"\$@\"" > "${BIN_DIR}/${APP_NAME}"
chmod +x "${BIN_DIR}/${APP_NAME}"

# Create DEBIAN control file
cat <<EOF > "${CONTROL_FILE}"
Package: ${APP_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: ${ARCH}
Depends: python3, python3-bs4
Maintainer: Mahros Alqabasy <your.email@example.com>
Description: A CLI tool to extract <iframe> elements from HTML files.
EOF

# Build the .deb
dpkg-deb --build "${BUILD_DIR}"

echo "Package built at: dist/${PKG_NAME}.deb"
