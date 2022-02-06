cmake_minimum_required(VERSION 3.1.0)							

project(squirrel)

#INCLUDE(conanbuildinfo.cmake)
#conan_basic_setup()
	
set(SRC_LIST 
	sqapi.cpp
    sqbaselib.cpp
    sqclass.cpp
    sqcompiler.cpp
    sqdebug.cpp
    sqfuncstate.cpp
    sqlexer.cpp
    sqmem.cpp
    sqobject.cpp
    sqstate.cpp
    sqtable.cpp
    sqvm.cpp
)

set(HEADER_FILES  
    sqarray.h
    sqclass.h
    sqclosure.h
    sqcompiler.h
    sqfuncproto.h
    sqfuncstate.h
    sqlexer.h
    sqobject.h
    sqopcodes.h
    sqpcheader.h
    sqstate.h
    sqstring.h
    sqtable.h
    squserdata.h
    squtils.h
    sqvm.h
)

include_directories(${CMAKE_SOURCE_DIR}/include/)

if (MSVC) 
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
    set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL} /MT")
    set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO} /MT")
endif()

ADD_LIBRARY(squirrel STATIC ${SRC_LIST})
			 
			 

			 
			 