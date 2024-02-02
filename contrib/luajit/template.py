pkgname = "luajit"
_pkgver = "2.1-20230410"
pkgver = _pkgver.replace("-", ".")
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "amalg"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Just-In-Time Compiler for Lua"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/openresty/luajit2"
source = f"{url}/archive/refs/tags/v{_pkgver}.tar.gz"
sha256 = "77bbcbb24c3c78f51560017288f3118d995fe71240aa379f5818ff6b166712ff"
# tests need luajit to be installed before they can be run
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_man("etc/luajit.1")


@subpackage("luajit-devel")
def _devel(self):
    return self.default_devel()
