pkgname = "xreader"
pkgver = "4.2.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX: drop libexec
    "-Dcomics=true",
    "-Ddjvu=true",
    "-Dmathjax-directory=/usr/share/yelp/mathjax",
    "-Dpixbuf=true",
]
hostmakedepends = ["intltool", "meson", "pkgconf"]
makedepends = [
    "cairo-devel",
    "djvulibre-devel",
    "glib-devel",
    "gtk+3-devel",
    "libarchive-devel",
    "libgxps-devel",
    "libice-devel",
    "libsecret-devel",
    "libsm-devel",
    "libspectre-devel",
    "libtiff-devel",
    "libx11-devel",
    "libxml2-devel",
    "poppler-devel",
    "webkitgtk-devel",
    "xapp-devel",
    "zlib-ng-compat-devel",
]
depends = ["yelp"]
pkgdesc = "Generic document reader"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/xreader/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "57d8c20eddcb90ba768f386c444519b5f330c1aacfcaa3deb33db1ad1d7bbd6d"
# Tests require the "dogtail" Python module
options = ["!check"]


@subpackage("xreader-devel")
def _(self):
    return self.default_devel()
