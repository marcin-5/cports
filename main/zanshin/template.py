pkgname = "zanshin"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(akonadi-akonadi.*|editingtaskfeature|inboxpagemodeltest|alltaskspagemodeltest|migrationtest|pageviewtest)",
    "-j1",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-devel",
    "boost-devel",
    "kcalendarcore-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "krunner-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-devel",
]
checkdepends = [
    "dbus",
    "kdepim-runtime",
]
pkgdesc = "KDE time management assistant"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://zanshin.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/zanshin-{pkgver}.tar.xz"
sha256 = "f76f95b0c73a798d1fb9dcc05367456ace322296f3ecaa68c34f3d6a66404158"
