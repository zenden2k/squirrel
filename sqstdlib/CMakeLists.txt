cmake_minimum_required(VERSION 3.1.0)							

project(sqstdlib)
	
set(SRC_LIST 
	sqstdaux.cpp
    sqstdblob.cpp
    sqstdio.cpp
    sqstdmath.cpp
    sqstdrex.cpp
    sqstdstream.cpp
    sqstdstring.cpp
    sqstdsystem.cpp
)

set(HEADER_FILES  
	sqstdblobimpl.h
	sqstdstream.h
)

include_directories(${CMAKE_SOURCE_DIR}/include/)

if (MSVC) 
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MTd")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
    set(CMAKE_CXX_FLAGS_MINSIZEREL "${CMAKE_CXX_FLAGS_MINSIZEREL} /MT")
    set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO} /MT")
endif()

ADD_LIBRARY(sqstdlib STATIC ${SRC_LIST})
			 
			 

			 
			 