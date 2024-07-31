from conan import ConanFile

class CcConanfile(ConanFile):
    name = "cc"
    version = "1.0"
    description = "a c compiler"
    license = "none"
    homepage = "none"

    settings = ["os", "arch"]

    def build_requirements(self):
        if self.settings.os.glibc == "bootstrap":
            return
        else:
            self.tool_requires("cc/1.0")
