//
// Created by lwz on 18-8-27.
//
#include <stdio.h>
#include <ctype.h>

#ifndef DATASTRUCT_TEST_H
#define DATASTRUCT_TEST_H
#define NO 0  // Macro define
#define YES 1
#define SIZE 10
//#undef name  // declare not marcro

#define BUFSIZE 100
char buf[BUFSIZE];
int bufp = 0;
/* buffer for ungetch */
/* next free position in buf */
int f_register();
void swap(int *px, int *py);

int getch(void) /* get a (possibly pushed-back) character */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}


void ungetch(int c)
/* push character back on input */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

/* getint: get next integer from input into *pn */
int getint(int *pn) {
    int c, sign;
    while (isspace(c = getch()))
/* skip white space */
        ;
    if (!isdigit(c) && c != EOF && c != '+' && c != '-') {
        ungetch(c); /* it is not a number */
        return 0;
    }
    sign = (c == '-') ? -1 : 1;
    if (c == '+' || c == '-')
        c = getch();
    for (*pn = 0; isdigit(c); c = getch())
        *pn = 10 * *pn + (c - '0');
    *pn *= sign;
    if (c != EOF)
        ungetch(c);
    return c;
}

/* strlen: return length of string s */
//int strlen(char *s) {
//    int n;
//    for (n = 0; *s != '\0'; s++){ n++;}
//    return n;
//}

//int *f(); /* f: function returning pointer to int */
//int (*pf)(); /* pf: pointer to function returning int */
//char **argv; // argv: pointer to char
//int (*daytab)[13]; //daytab: pointer to array[13] of int
//int *daytab[13]; // daytab: array[13] of pointer to int
//void *comp(); //comp: function returning pointer to void
//void (*comp)(); // comp: pointer to function returning void
//char (*(*x())[])(); // x: function returning pointer to array[] of  pointer to function returning char
//char (*(*x[3])())[5]; //x: array[3] of pointer to function returning pointer to array[5] of char

/*
    #if SYSTEM == SYSV
    #define HDR "sysv.h"
    #elif SYSTEM == BSD
    #define HDR "bsd.h"
    #elif SYSTEM == MSDOS
    #define HDR "msdos.h"
    #else
    #define HDR "default.h"
    #endif
    #include HDR
*/
#endif //DATASTRUCT_TEST_H

void hello_world(){
    printf("hello world! \n");
}
