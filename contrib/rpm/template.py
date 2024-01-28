pkgname = "rpm"
pkgver = "4.19.1"
_pkgvx = "4.19.x"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_NLS=OFF",
    "-DWITH_ACL=OFF",
    "-DWITH_AUDIT=OFF",
    "-DWITH_CAP=OFF",
    "-DWITH_DBUS=OFF",
    "-DWITH_IMAEVM=OFF",
    "-DWITH_FAPOLICYD=OFF",
    "-DWITH_FSVERITY=OFF",
    "-DWITH_SELINUX=OFF",
    "-DRPM_VENDOR=Chimera Linux",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext", "podman"]
makedepends = [
    "bzip2-devel",
    "elfutils-devel",
    "file-devel",
    "libarchive-devel",
    "libomp-devel",
    "lua5.4-devel",
    "popt-devel",
    "python-devel",
    "sqlite-devel",
    "xz-devel",
    "zlib-devel",
    "zstd-devel",
    "rpm-sequoia-devel",
]
pkgdesc = "RPM Package Manager"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
# rpm is GPL, librpm is GPL-or-LGPL
license = "GPL-2.0-or-later OR LGPL-2.0-or-later"
url = "https://rpm.org"
source = f"http://ftp.rpm.org/releases/rpm-{_pkgvx}/rpm-{pkgver}.tar.bz2"
sha256 = "4de4dcd82f2a46cf48a83810fe94ebda3d4719b45d547ed908b43752a7581df1"
