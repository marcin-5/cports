pkgname = "texstudio"
pkgver = "4.8.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "hunspell-devel",
    "poppler-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "quazip-devel",
]
pkgdesc = "Integrated writing environment for creating LaTeX documents"
license = "GPL-3.0-or-later"
url = "https://www.texstudio.org"
source = f"https://github.com/texstudio-org/texstudio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ea09549e65a11520995a5b542f88ac4d21ea550c070008e1087add87856db02f"
