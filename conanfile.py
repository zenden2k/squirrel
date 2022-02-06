from conans import ConanFile, CMake

class SquirrelConan(ConanFile):
    name = "squirrel"
    version = "3.0.0"
    license = "Apache-2.0"
    url = "http://squirrel-lang.org/"
    description = "Squirrel is a high level imperative, object-oriented programming language."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "squirrel/*", "sqstdlib/*", "include/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # Explicit way:
        # self.run('cmake "%s/src" %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info
        self.cpp_info.components["sqstdlib"].libs = ["sqstdlib"]      
        self.cpp_info.components["sqstdlib"].requires = ["Squirrel"]
        self.cpp_info.components["sqstdlib"].defines= ["_SQ64"]
        self.cpp_info.components["Squirrel"].libs = ["squirrel"] 
        self.cpp_info.components["Squirrel"].defines= ["_SQ64"]