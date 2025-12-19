pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.26.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DTREE_SITTER_FEATURE_WASM=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["wasmtime-devel"]
pkgdesc = "Incremental parsing library for language grammars"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "7f4a7cf0a2cd217444063fe2a4d800bc9d21ed609badc2ac20c0841d67166550"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
