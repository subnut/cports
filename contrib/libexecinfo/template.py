pkgname = "libexecinfo"
pkgver = "1.0.20200314"
_gitrev = "7e6781ac86c4ebea531b0c9ea52c23452f8bfc6e"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Provides execinfo.h for MUSL systems"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/ronchaine/libexecinfo"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "59648d745acbda0af0188c8d011e3c54b06db973acbb27d87fed4d21b0f8ba66"
# no testsuite
options = ["!check"]


def post_extract(self):
    self.do("sh", "-c", "sed -n '2,24s/[*]//p' execinfo.h > LICENSE")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libexecinfo-static")
def _static(self):
    return self.default_static()
