from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools


class AppConan(ConanFile):
    name = "app"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*"
    requires = "hello/0.1@user/testing"

    def build_requirements(self):
        if self.settings.os == "Windows":
            self.build_requires("make/4.2.1")

    def build(self):
        with tools.chdir("src"):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make()

    def package(self):
        self.copy("*app", dst="bin", keep_path=False)
        self.copy("*app.exe", dst="bin", keep_path=False)

    def deploy(self):
        self.copy("*", src="bin", dst="bin")