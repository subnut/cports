pkgname = "gwenview"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(placetreemodeltest|urlutilstest|contextmanagertest)",
]
make_check_wrapper = [
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "baloo-devel",
    # "cfitsio-devel",
    "exiv2-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kimageannotator-devel",
    "kio-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kparts-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "libkdcraw-devel",
    "libtiff-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "purpose-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE image viewer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/gwenview"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/gwenview-{pkgver}.tar.xz"
sha256 = "18d10edb4f7492105a28cb1de114331b7cebf129ce626b8779e1fd75199e7476"
# avoid crash in raw thumbnailer
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["vis"]
# TODO
options = ["!cross"]
