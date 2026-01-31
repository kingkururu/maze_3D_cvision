cmake_minimum_required(VERSION 3.10)
project(maze_3D_cvision VERSION 1.0 LANGUAGES CXX)
list(APPEND CMAKE_PREFIX_PATH "/opt/homebrew")

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 1. --- Dependencies ---
find_package(SFML 2.6 COMPONENTS graphics window system audio REQUIRED)
find_package(spdlog REQUIRED)
find_package(fmt REQUIRED)
find_package(yaml-cpp REQUIRED)

# --- Added Python Support ---
find_package(Python3 COMPONENTS Development Interpreter REQUIRED)

# 2. --- Source Files ---
set(RUN_SOURCES
    test/test-src/testMain.cpp
    test/test-src/game/globals/globals.cpp
    test/test-src/game/core/game.cpp
    test/test-src/game/physics/physics.cpp
    test/test-src/game/camera/window.cpp
    test/test-src/game/utils/utils.cpp
    test/test-src/game/scenes/scenes.cpp
    test/test-src/game/vision/vision.cpp
    test/test-assets/sprites/sprites.cpp
    test/test-assets/fonts/fonts.cpp
    test/test-assets/sound/sound.cpp
    test/test-assets/tiles/tiles.cpp
    test/test-logging/log.cpp
)

# 3. --- Executable Target ---
add_executable(run ${RUN_SOURCES})

# 4. --- Preprocessor Definitions ---
target_compile_definitions(run PRIVATE TESTING)

# 5. --- Include Directories ---
target_include_directories(run PRIVATE
    ./test/test-src
    ./test/test-src/game/core
    ./test/test-src/game/camera
    ./test/test-src/game/globals
    ./test/test-src/game/physics
    ./test/test-src/game/scenes
    ./test/test-src/game/utils
    ./test/test-src/game/vision
    ./test/test-assets
    ./test/test-assets/fonts
    ./test/test-assets/sound
    ./test/test-assets/tiles
    ./test/test-assets/sprites
    ./test/test-logging
    ${Python3_INCLUDE_DIRS} # Added Python headers
)

# 6. --- Link Libraries ---
target_link_libraries(run PRIVATE
    sfml-graphics
    sfml-window
    sfml-system
    sfml-audio
    spdlog::spdlog
    fmt::fmt
    yaml-cpp::yaml-cpp
    Python3::Python # Added Python library
)

# 7. --- Copy Config & Python Files ---
add_custom_command(TARGET run POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E make_directory $<TARGET_FILE_DIR:run>/config
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_CURRENT_SOURCE_DIR}/test/test-src/game/globals/config.yaml
        $<TARGET_FILE_DIR:run>/config/config.yaml
    
    # UPDATE THIS LINE BELOW:
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_CURRENT_SOURCE_DIR}/test/test-src/game/vision/vision.py 
        $<TARGET_FILE_DIR:run>/vision.py
        
    COMMENT "Copying config and Python script to build directory..."
)

# NEW: Copy your python file to the build directory so the C++ app can find it
add_custom_command(TARGET run POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_if_different
        ${CMAKE_CURRENT_SOURCE_DIR}/test/test-src/game/vision/vision.py 
        $<TARGET_FILE_DIR:run>/vision.py
    COMMENT "Copying Python script to build directory..."
)

# This copies 'test' folder into the 'build' folder
add_custom_command(TARGET run POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory
        ${CMAKE_CURRENT_SOURCE_DIR}/test
        $<TARGET_FILE_DIR:run>/test
    COMMENT "Syncing assets to build directory..."
)