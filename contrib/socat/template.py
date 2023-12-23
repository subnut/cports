pkgname = "socat"
pkgver = "1.8.0.0"
pkgrel = 1
build_style = "configure"
make_install_args = ["prefix=/usr"]
make_check_target = "test"
makedepends = ["linux-headers", "openssl-devel", "readline-devel"]
checkdepends = ["bash", "iproute2", "procps"]
pkgdesc = "Multipurpose relay for bidirectional binary data transfer (netcat++)"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-only"
url = "http://www.dest-unreach.org/socat"
source = f"{url}/download/socat-{pkgver}.tar.bz2"
sha256 = "e1de683dd22ee0e3a6c6bbff269abe18ab0c9d7eb650204f125155b9005faca7"
hardening = ["vis", "cfi"]


def post_extract(self):
    # tests 478 and 528 fail due to stdout not being a tty
    self.do(
        "sed",
        "-i",
        ".bak",
        "/^test:/,+1s|./test.sh|& --expect-fail 478,528|",
        "Makefile.in",
    )
    # test.sh uses $USER, which is unset in the environment
    # if $USER is unset, test 418 fails (due to user=$USER argument of socat)
    #
    # but if $USER is set, test 217 fails, and I've got NO IDEA WHY!
    self.do("sed", "-i", ".in", "s/$USER/$(whoami)/g", "test.sh")
