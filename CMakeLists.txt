cmake_minimum_required(VERSION 3.1.0)							

project(squirrel)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_definitions(-D_LIB -DGARBAGE_COLLECTOR -D_SQ64)

add_subdirectory(squirrel)	
add_subdirectory(sqstdlib)	


			 
			 