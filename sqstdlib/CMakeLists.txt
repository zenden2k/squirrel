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

ADD_LIBRARY(sqstdlib STATIC ${SRC_LIST})
			 
			 

			 
			 