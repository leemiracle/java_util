//
// Created by lwz on 18-8-27.
//
#include "test.h"

int main(){
    int x = 1, y = 2, z[10]; // '&' get the address of value, '*' get the content of point
    int *ip;
//    ip = &x;
//    y = *ip;
//    *ip = 1;
//    ip = &z[0];
//    printf("%d\t%d\t%d\t%d\t%d\t\n", x, y, z[0], &ip, *ip);
    int *iq;
    ip = &x;
    iq = &y;
//    swap(x, y); // need point variable
    swap(ip, iq); // swap x and y
    printf("%d\t%d\n", x, y);

    int n, array[SIZE], getint(int *);
    for (n = 0; n < SIZE && getint(&array[n]) != EOF; n++)
        ;
    char * ptr;
    strlen("hello, world");
    strlen(array);
    strlen(ptr);
}

void swap(int *px, int *py){
    int temp;
    temp = *px;
    *px = *py;
    *py = temp;
}

