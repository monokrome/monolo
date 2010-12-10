###
# TODO: Add support for Windows compilers.

# Our source directory should be where our source files are - not our build files.
SET(CMAKE_BOOTSTRAP_DIR "${CMAKE_SOURCE_DIR}")
SET(CMAKE_SOURCE_DIR "${CMAKE_SOURCE_DIR}/../../src/")

# Requires that we build this file outside of our source tree
INCLUDE("${CMAKE_BOOTSTRAP_DIR}/RequireOutOfSource.cmake")

CMAKE_MINIMUM_REQUIRED (VERSION 2.8)
PROJECT (MONOLO)

# Add a 'DEBUG' definition when applicable
IF (CMAKE_BUILD_TYPE STREQUAL "Debug" OR CMAKE_BUILD_TYPE STREQUAL "RelWithDebInfo")
	ADD_DEFINITIONS(-DDEBUG)
ENDIF()

