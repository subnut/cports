pkgname = "massren"
pkgver = "1.5.6"
pkgrel = 0
build_style = "go"
make_build_args = ["-tags", "libsqlite3 linux"]
make_check_args = make_build_args
hostmakedepends = ["go"]
makedepends = ["sqlite-devel"]
pkgdesc = "Rename multiple files using your text editor"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/laurent22/massren"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "49758b477a205f3fbf5bbe72c2575fff8b5536f8c6b45f8f6bd2fdde023ce874"


def post_extract(self):
    self.rm("vendor", True)


def pre_prepare(self):
    self.do("go", "mod", "init")
    self.do("go", "mod", "tidy", allow_network=True)


def post_install(self):
    self.install_license(self.files_path / "LICENSE")
