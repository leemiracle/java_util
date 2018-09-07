 cmake_minimum_required(VERSION 3.5)

PROJECT(HELLO)
ADD_SUBDIRECTORY(src bin) #当前工程子目录(source_dir)/中间二进制和目标二进制存放位置/ : ADD_SUBDIRECTORY(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
 # SET 指令重新定义 EXECUTABLE_OUTPUT_PATH 和 LIBRARY_OUTPUT_PATH 变量(最终的二进制的位置): 在哪里 ADD_EXECUTABLE 或 ADD_LIBRARY,需要改变目标存放路径,就加上述定义
 #   SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
 #   SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

 #安装: 变量CMAKE_INSTALL_PREFIX/ configure 脚本的 – prefix / cmake -DCMAKE_INSTALL_PREFIX=/usr .
 #install指令:INSTALL 指令用于定义安装规则,安装的内容可以包括目标二进制、动态库、静态库以及文件、目录、脚本等
