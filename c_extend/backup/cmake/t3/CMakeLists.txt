 cmake_minimum_required(VERSION 3.5) # 构建动态库和静态库: gcc参数直接构建
 PROJECT(HELLOLIB)
 ADD_SUBDIRECTORY(lib) # 指定编译输出位置/SET(LIBRARY_OUTPUT_PATH <路径>)来指定一个新的位置