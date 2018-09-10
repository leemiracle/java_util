cmake_minimum_required(VERSION 3.0)
# 基本语法规则(任何一个目录建CMakeLists.txt):
#   ${}方式取值,
#   指令(参数 1 参数 2...) 括号括住,空格或分号分开, 指令大小写无关,变量大小写相关,如果变量等有空格需双引号
#   工程名和可执行文件没有任何关系
#   所谓外部构建就是在工程源码外放build

#PROJECT (HELLO) # 指令定义:工程名/工程支持的语言列表：PROJECT(projectname [CXX] [C] [Java])
##隐式定义了两个变量(建议使用固定的变量名): 编译路径<projectname>_BINARY_DIR 以及 工程路径<projectname>_SOURCE_DIR
#
#SET(SRC_LIST main.c) # 显式的定义变量(多个源文件:SET(SRC_LIST main.c t1.c t2.c)): SET(VAR [VALUE] [CACHE TYPE DOCSTRING [FORCE]])
#
#MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR}) # 终端输出用户定义的信息: MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display" ...)
#MESSAGE(STATUS "This is SOURCE dir " ${HELLO_SOURCE_DIR}) #     (SEND_ERROR,产生错误,生成过程被跳过,  SATUS ,输出前缀为 — 的信息, FATAL_ERROR,立即终止所有 cmake 过程)
#
#ADD_EXECUTABLE(hello ${SRC_LIST})

# cmake . 开始构建【makefile】
# make VERBOSE=1: 查看make构建详情

project(c_extend)
add_subdirectory(cpu_features)
#set(_HDRS
#    include/cpuinfo_aarch64.h
#    include/cpuinfo_arm.h
#    include/cpuinfo_mips.h
#    include/cpuinfo_ppc.h
#    include/cpuinfo_x86.h
#    include/cpu_features_macros.h
#)
#
#add_library(cpu_features
#    ${_HDRS}
#    include/internal/bit_utils.h
#    include/internal/linux_features_aggregator.h
#    include/internal/cpuid_x86.h
#    include/internal/filesystem.h
#    include/internal/hwcaps.h
#    include/internal/stack_line_reader.h
#    include/internal/string_view.h
#    include/cpu_features_macros.h
#    src/linux_features_aggregator.c
#    src/cpuid_x86_clang_gcc.c
#    src/cpuid_x86_msvc.c
#    src/cpuinfo_aarch64.c
#    src/cpuinfo_arm.c
#    src/cpuinfo_mips.c
#    src/cpuinfo_ppc.c
#    src/cpuinfo_x86.c
#    src/filesystem.c
#    src/hwcaps.c
#    src/stack_line_reader.c
#    src/string_view.c
#)
