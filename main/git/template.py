pkgname = "git"
pkgver = "2.49.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dcontrib=completion,contacts,subtree",
    "-Dcredential_helpers=libsecret",
    "-Ddocs=man",
]
hostmakedepends = [
    "asciidoc",
    "cmake",
    "gettext",
    "meson",
    "perl",
    "pkgconf",
    "tk",
    "xmlto",
]
makedepends = [
    "curl-devel",
    "libexpat-devel",
    "libsecret-devel",
    "pcre2-devel",
    "tk-devel",
    "zlib-ng-devel",
]
depends = [
    "ca-certificates",
    "perl-authen-sasl",
    "perl-mime-tools",
    "perl-net-smtp-ssl",
]
checkdepends = ["gnupg", "gsed"]
pkgdesc = "Fast, distributed version control system"
license = "GPL-2.0-only"
url = "https://git-scm.com"
source = f"https://www.kernel.org/pub/software/scm/git/git-{pkgver}.tar.xz"
sha256 = "618190cf590b7e9f6c11f91f23b1d267cd98c3ab33b850416d8758f8b5a85628"
hardening = ["cfi", "vis"]


@subpackage("git-gitk")
def _(self):
    self.depends += [self.parent, "tk"]
    self.pkgdesc = "Git repository browser"
    self.provides = [self.with_pkgver("gitk")]
    self.license = "GPL-2.0-or-later"
    return ["usr/bin/gitk", "usr/share/gitk", "usr/share/man/man1/gitk.1"]


# @subpackage("git-gui")
# def _(self):
#     self.depends += [self.parent, "tk"]
#     self.subdesc = "GUI tool"
#     self.license = "GPL-2.0-or-later"
#     return [
#         "usr/lib/git-core/git-gui*",
#         "usr/lib/git-core/git-citool",
#         "usr/share/man/man1/git-gui.1",
#         "usr/share/man/man1/git-citool.1",
#         "usr/share/git-gui",
#     ]


@subpackage("git-credential-libsecret")
def _(self):
    self.depends += [self.parent]
    self.install_if = [self.parent, "libsecret"]
    self.pkgdesc = "Git libsecret credential helper"

    return ["usr/lib/git-core/git-credential-libsecret"]


@subpackage("git-scalar")
def _(self):
    self.depends += [self.parent]
    self.pkgdesc = "Git scalar monorepo tool"

    return [
        "usr/bin/scalar",
        "usr/lib/git-core/scalar",
    ]


@subpackage("git-svn")
def _(self):
    self.subdesc = "Subversion support"
    self.depends += [self.parent, "subversion-perl", "perl-termreadkey"]
    self.install_if = [self.parent, "subversion"]

    return [
        "usr/share/perl5/vendor_perl/Git/SVN*",
        "usr/lib/git-core/git-svn",
        "usr/share/man/man1/git-svn.1",
    ]
