pkgname = "dmd-bootstrap"
pkgver = "2.069.20180305"
_gitrev = {
    "dmd": "75266348c8a2368945a339ab86d7c8960a9bfc08",
    "phobos": "30ac23a0889dd183221ce531a057171dd45296c4",
    "druntime": "33ae38cef41564b12864470afaf8430eb7334d3b",
}
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "-fposix.mak",
    "RELEASE=1",
    "WARNINGS=-Wno-c++11-narrowing",
    "WARNINGS+=-Wno-register",
]
make_install_args = [
    "-fposix.mak",
    "RELEASE=1",
]
hostmakedepends = ["gmake"]
pkgdesc = "D Programming Language compiler (Bootstrap version)"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSL-1.0"
url = "https://dlang.org"
source = [
    f"https://github.com/dlang/{pkg}/archive/{_gitrev[pkg]}.tar.gz>{pkg}.tar.gz"
    for pkg in ("dmd", "phobos", "druntime")
]
source_paths = ["dmd", "phobos", "druntime"]
sha256 = [
    "015ad5ce9d60bc183b9b40ae649eafeced93cb2a211400d9280464b22acdb129",
    "57306f80a63b83b755043d05e85e83cf3178701c92d295c97d1a5a8be8ffce19",
    "7f4d84f2b5252c0cc33bffbb4de8aab9321df844b8512e27e90267cbb9bc7422",
]
patch_args = ["-p0"]
# no testsuite
options = ["!check", "!lintstatic"]


def do_build(self):
    self.make_use_env = True
    with self.pushd("dmd/src"):
        self.make_build_target = "inifile.o"
        self.make_build_args.append("CXXFLAGS+=-DSYSCONFDIR='\"/etc\"'")
        self.make.build()
        self.make_build_args.pop()
        self.make_build_target = ""
    with self.pushd("dmd/src"):
        self.make.build()
    with self.pushd("phobos"):
        self.make.build()


def do_install(self):
    self.make_use_env = False
    self.make_install_args.append(f"LIBDIR={self.chroot_destdir / 'usr/lib'}")
    for path in source_paths:
        with self.pushd(path):
            self.make.install()
    with self.pushd("install"):
        # for file in self.find("man", "man?/*"):
        #     self.install_man(file)
        self.install_bin("bin/dmd")
        self.install_license("dmd-boostlicense.txt", "LICENSE.txt")
        self.install_license("dmd-backendlicense.txt", "backendlicense.txt")
        with self.pushd("src"):
            self.install_files("phobos", "usr/include/dmd")
            with self.pushd("druntime"):
                self.mv("import", "druntime")
                self.install_files("druntime", "usr/include/dmd")
    self.install_dir("etc")
    self.install_file(self.files_path / "dmd.conf", "etc")
