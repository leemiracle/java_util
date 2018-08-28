cmake_minimum_required(VERSION 3.12)
project(dataStruct C)

set(CMAKE_C_STANDARD 99)

add_executable(dataStruct basic.c linear_list.c type_operator_expression.c test.h function.c test.c point_arrays.c struct_typedef_union.c)