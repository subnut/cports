pkgname = "prison"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "libdmtx-devel",
    "qrencode-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE library to produce QR codes and DataMatrix barcodes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://api.kde.org/frameworks/prison/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/prison-{pkgver}.tar.xz"
sha256 = "bbc17dccfb71988af41e70110b6635323e17d8ed48c08f73808f9f220fb067ba"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("prison-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
