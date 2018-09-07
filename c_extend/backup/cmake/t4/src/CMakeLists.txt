ADD_EXECUTABLE(main main.c)

INCLUDE_DIRECTORIES(/usr/include/hello) # 找到指定的头文件:INCLUDE_DIRECTORIES([AFTER|BEFORE] [SYSTEM] dir1 dir2 ...)
# 未连接到共享库libhello上:main.c:(.text+0xa)：对‘HelloFunc’未定义的引用
#LINK_DIRECTORIES(dirxx) # 添加非标准的共享库搜索路径(也可以TARGET_LINK_LIBRARIES(main hello) )
#TARGET_LINK_LIBRARIES(main hello) # 目标文件link到共享库[查看link情况:ldd src/main]
TARGET_LINK_LIBRARIES(main libhello.a) #链接静态库

# 系统环境变量(用于find_指令): CMAKE_INCLUDE_PATH 和 CMAKE_LIBRARY_PATH
# bash: export CMAKE_INCLUDE_PATH=/usr/include/hello
# cmake:
#   FIND_PATH(myHeader hello.h)
#   IF(myHeader)
#       INCLUDE_DIRECTORIES(${myHeader})
#   ENDIF(myHeader)

# 常用变量:路径/cmake模块/项目
# 调用环境变量: $ENV{NAME} / 当前路径相关 / 系统信息 / 主要的开关选项 /
# 常用指令:
#   ADD_DEFINITIONS: 编译器-D定义
#   ADD_DEPENDENCIES: 依赖(确保其他target被构建)[ADD_EXECUTABLE、ADD_LIBRARY、ADD_SUBDIRECTORY]
#   ADD_TEST(testname Exename arg1 arg2 ...)[ENABLE_TESTING]
#   AUX_SOURCE_DIRECTORY: 目录下所有源码存储在一个变量里
#   CMAKE_MINIMUM_REQUIRED
#   EXEC_PROGRAM:处理过程中执行命令
#   FILE :文件操作
#   INCLUDE:载入cmakelists文件/载入预定义的cmake模块
#   INSTALL:
#   find_:
#   控制:1,IF 2,WHILE  3,FOREACH

