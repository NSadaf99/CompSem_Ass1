# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/fast_align

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/fast_align/build

# Include any dependencies generated for this target.
include CMakeFiles/fast_align.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/fast_align.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fast_align.dir/flags.make

CMakeFiles/fast_align.dir/src/fast_align.cc.o: CMakeFiles/fast_align.dir/flags.make
CMakeFiles/fast_align.dir/src/fast_align.cc.o: ../src/fast_align.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/fast_align/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fast_align.dir/src/fast_align.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fast_align.dir/src/fast_align.cc.o -c /root/fast_align/src/fast_align.cc

CMakeFiles/fast_align.dir/src/fast_align.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fast_align.dir/src/fast_align.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/fast_align/src/fast_align.cc > CMakeFiles/fast_align.dir/src/fast_align.cc.i

CMakeFiles/fast_align.dir/src/fast_align.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fast_align.dir/src/fast_align.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/fast_align/src/fast_align.cc -o CMakeFiles/fast_align.dir/src/fast_align.cc.s

CMakeFiles/fast_align.dir/src/fast_align.cc.o.requires:

.PHONY : CMakeFiles/fast_align.dir/src/fast_align.cc.o.requires

CMakeFiles/fast_align.dir/src/fast_align.cc.o.provides: CMakeFiles/fast_align.dir/src/fast_align.cc.o.requires
	$(MAKE) -f CMakeFiles/fast_align.dir/build.make CMakeFiles/fast_align.dir/src/fast_align.cc.o.provides.build
.PHONY : CMakeFiles/fast_align.dir/src/fast_align.cc.o.provides

CMakeFiles/fast_align.dir/src/fast_align.cc.o.provides.build: CMakeFiles/fast_align.dir/src/fast_align.cc.o


CMakeFiles/fast_align.dir/src/ttables.cc.o: CMakeFiles/fast_align.dir/flags.make
CMakeFiles/fast_align.dir/src/ttables.cc.o: ../src/ttables.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/fast_align/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/fast_align.dir/src/ttables.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fast_align.dir/src/ttables.cc.o -c /root/fast_align/src/ttables.cc

CMakeFiles/fast_align.dir/src/ttables.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fast_align.dir/src/ttables.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/fast_align/src/ttables.cc > CMakeFiles/fast_align.dir/src/ttables.cc.i

CMakeFiles/fast_align.dir/src/ttables.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fast_align.dir/src/ttables.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/fast_align/src/ttables.cc -o CMakeFiles/fast_align.dir/src/ttables.cc.s

CMakeFiles/fast_align.dir/src/ttables.cc.o.requires:

.PHONY : CMakeFiles/fast_align.dir/src/ttables.cc.o.requires

CMakeFiles/fast_align.dir/src/ttables.cc.o.provides: CMakeFiles/fast_align.dir/src/ttables.cc.o.requires
	$(MAKE) -f CMakeFiles/fast_align.dir/build.make CMakeFiles/fast_align.dir/src/ttables.cc.o.provides.build
.PHONY : CMakeFiles/fast_align.dir/src/ttables.cc.o.provides

CMakeFiles/fast_align.dir/src/ttables.cc.o.provides.build: CMakeFiles/fast_align.dir/src/ttables.cc.o


# Object files for target fast_align
fast_align_OBJECTS = \
"CMakeFiles/fast_align.dir/src/fast_align.cc.o" \
"CMakeFiles/fast_align.dir/src/ttables.cc.o"

# External object files for target fast_align
fast_align_EXTERNAL_OBJECTS =

fast_align: CMakeFiles/fast_align.dir/src/fast_align.cc.o
fast_align: CMakeFiles/fast_align.dir/src/ttables.cc.o
fast_align: CMakeFiles/fast_align.dir/build.make
fast_align: CMakeFiles/fast_align.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/fast_align/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable fast_align"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fast_align.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fast_align.dir/build: fast_align

.PHONY : CMakeFiles/fast_align.dir/build

CMakeFiles/fast_align.dir/requires: CMakeFiles/fast_align.dir/src/fast_align.cc.o.requires
CMakeFiles/fast_align.dir/requires: CMakeFiles/fast_align.dir/src/ttables.cc.o.requires

.PHONY : CMakeFiles/fast_align.dir/requires

CMakeFiles/fast_align.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fast_align.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fast_align.dir/clean

CMakeFiles/fast_align.dir/depend:
	cd /root/fast_align/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/fast_align /root/fast_align /root/fast_align/build /root/fast_align/build /root/fast_align/build/CMakeFiles/fast_align.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fast_align.dir/depend

