from conan import ConanFile

class FooConanfile(ConanFile):
    name = "foo"
    version = "1.0"
    description = "something that needs a compiler"
    license = "none"
    homepage = "none"

    def build_requirements(self):
        self.tool_requires("cc/1.0")

