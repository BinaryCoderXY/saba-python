cmake_minimum_required(VERSION 3.18)
project(mmd_wrap)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(PYTHON_EXECUTABLE python3.12)

find_package(OpenGL)
find_package(OpenGL REQUIRED)
include_directories(${OPENGL_INCLUDE_DIR})
add_subdirectory(saba/external/glfw)
add_subdirectory(saba)
# 编译 saba
add_subdirectory(pybind11)
include_directories(.)
include_directories(saba/src)
include_directories(saba/external)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/src)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/glm/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/spdlog/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/imgui)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/stb/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/gl3w/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/glew/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/external/glfw/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/saba/viewer)
include_directories(saba/viewer/Saba/GL/Model/MMD/)
# 构建 Python 模块
pybind11_add_module(saba
    mmd_wrap.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/saba/external/gl3w/src/gl3w.c
)

# 链接 saba
target_link_libraries(saba PRIVATE Saba)
# 复制resource资源文件夹到安装目录
install(DIRECTORY ${CMAKE_BINARY_DIR}/saba/resource
    DESTINATION resource
)