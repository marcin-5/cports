pkgname = "gocryptfs"
pkgver = "2.5.1"
pkgrel = 4
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X main.GitVersion={pkgver}"
    + " -X main.GitVersionFuse=[vendored]",
    ".",
    "./gocryptfs-xray",
]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["openssl3-devel"]
depends = ["fuse"]
pkgdesc = "Encrypted overlay filesystem"
license = "MIT"
url = "https://github.com/rfjakob/gocryptfs"
source = (
    f"{url}/releases/download/v{pkgver}/gocryptfs_v{pkgver}_src-deps.tar.gz"
)
sha256 = "80c3771c9f7e65af9326b107ddb7a30e9c3c7bf8823412b9615b7f77352cdde7"
# requires fuse kernel module
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = "vendor/github.com/aperturerobotics/jacobsa-crypto/cmac/hash.go:97:3: undefined: xorBlock"


def post_install(self):
    self.install_man("Documentation/gocryptfs.1")
    self.install_man("Documentation/gocryptfs-xray.1")
    self.install_license("LICENSE")
