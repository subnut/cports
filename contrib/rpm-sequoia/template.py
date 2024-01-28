pkgname = "rpm-sequoia"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "RPM Package Manager OpenPGP backend using Sequoia PGP"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://sequoia-pgp.org"
source = f"https://github.com/rpm-software-management/rpm-sequoia/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "be6362c38744635e56fd2fcce5428a6e3058cc52798311ceefbe236fe7890250"
env = {"PREFIX": "/usr"}


def post_build(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.mv(
            "librpm_sequoia.so",
            "librpm_sequoia.so." + pkgver.split(".")[0],
        )


def do_install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_file("rpm-sequoia.pc", "usr/lib/pkgconfig")
        self.install_lib("librpm_sequoia.so.*", glob=True)

    self.ln_s(
        "librpm_sequoia.so." + pkgver.split(".")[0],
        self.destdir / "usr/lib/librpm_sequoia.so",
    )


@subpackage("rpm-sequoia-devel")
def _devel(self):
    self.depends = ["openssl-devel", f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
