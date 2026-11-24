pkgname = "gram"
pkgver = "3.5.2"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
make_build_args = [
    *("-p", "cli"),
    *("-p", "gram"),
    *("-p", "remote_server"),
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "libxkbcommon-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Text editor forked from Zed"
license = "GPL-3.0-or-later"
url = "https://gram-editor.com"
source = f"https://codeberg.org/GramEditor/gram/archive/{pkgver}.tar.gz"
sha256 = "ba51b234cc2e947c68881675028fac9649216f601d205dd3b56083388a48697d"


def install(self):
    from cbuild.util import cargo

    srv = "gram-remote-server-{}-{}"
    with open(self.cwd / "crates/gram/RELEASE_CHANNEL") as f:
        srv = srv.format(f.read().strip(), self.pkgver)

    self.install_bin(cargo.target_path(self, "cli"), name="gram")
    self.install_lib(cargo.target_path(self, "gram"), name="gram-editor")
    self.install_bin(cargo.target_path(self, "remote_server"), name=srv)
    self.install_link("usr/bin/gram-remote-server", srv)

    with self.pushd("crates/gram/resources"):
        self.install_file(
            "app.liten.Gram.svg",
            "usr/share/icons/hicolor/scalable/apps",
        )
        self.install_file(
            "app.liten.Gram-symbolic.svg",
            "usr/share/icons/hicolor/symbolic/apps",
        )
        self.install_file(
            "app-icon.png",
            "usr/share/icons/hicolor/512x512/apps",
            name="app.liten.Gram.png",
        )
        self.install_file(
            "app-icon@2x.png",
            "usr/share/icons/hicolor/1024x1024/apps",
            name="app.liten.Gram.png",
        )
        self.install_file(
            "gram.desktop.in",
            "usr/share/applications",
            name="app.liten.Gram.desktop",
            pattern=r"\$(\w+)",
            template={
                "APP_ARGS": "%U",
                "APP_NAME": "Gram",
                "APP_ICON": "app.liten.Gram",
                "APP_CLI": "/usr/bin/gram",
            },
        )


@split("remote-server")
def _(self):
    self.subdesc = "remote server"
    return ["usr/bin/gram-remote-server*"]
