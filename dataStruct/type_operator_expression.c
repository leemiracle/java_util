//
// Created by lwz on 18-8-27.
//
#include <stdio.h>
#include <ctype.h>
#include <math.h>
/*
 * c++ learning websites
 *  http://www.cplusplus.com/reference/cstdio/printf/
 *
 */
 void max(int, int);
 void enum_test();

int main(){
    float eps = 1.0e-5;
//    enum_test();
    const char msg[] = "warning: ";
//    int year =2018;
//    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
//        printf("%d is a leap year\n", year);
//    else
//        printf("%d is not a leap year\n", year);

//    char c = 9; // not digit
//    char c = "9"; // error
//    char c = '9'; // isdigit
//    if(isdigit(c)){
//        printf("isdigit\n");
//    } else{
//        printf("not digit\n");
//    }
    printf("%.4e \n", sqrt(4.5)); // 格式化字符串 https://zh.wikipedia.org/wiki/%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2

    int b0 = 0b1010;
    int b1 = 0b1100;
    printf("%d\t%d\n", b0&b1, b1>>2);
    max(20, 30);

//    if(){
//    } else if(){
//
//    } else{
//
//    }
//    binsearch() // sorted list search
//    trim() // remove space character
//    goto and labels

/*
 * function definition
return-type function-name(argument declarations)
{
    declarations and statements
}
 */

}

void max(int a, int b) {
    int z = (a > b) ? a : b; /* z = max(a, b) */
    printf("max:%d\t\n",z);
}

void enum_test(){
    enum boolean {NO, YES};
    enum escapes { BELL = '\a', BACKSPACE = '\b', TAB = '\t',
        NEWLINE = '\n', VTAB = '\v', RETURN = '\r' }escape;
    /* FEB = 2, MAR = 3, etc. */
    enum months { JAN = 1, FEB, MAR, APR, MAY, JUN,
        JUL, AUG, SEP, OCT, NOV, DEC }month;
    for(escape=BELL; escape<= RETURN; escape++) {
        printf("%d\t", escape);
        printf("%c\t", escape); // escape is character
    }
    printf("\n");
    for(month=1; month<= DEC; month++) {
        switch (month) {
            case JAN:
                printf("%d\n", JAN);
                break;
            case FEB:
                printf("%d\n", FEB);
                break;
            case MAR:
                printf("%d\n", MAR);
                break;
            case APR:
                printf("%d\n", APR);
                break;
            case MAY:
                printf("%d\n", MAY);
                break;
            case JUN:
                printf("%d\n", JUN);
                break;
            case JUL:
                printf("%d\n", JUL);
                break;
            case AUG:
                printf("%d\n", AUG);
                break;
            case SEP:
                printf("%d\n", SEP);
                break;
            case OCT:
                printf("%d\n", OCT);
                break;
            case NOV:
                printf("%d\n", NOV);
                break;
            case DEC:
                printf("%d\n", DEC);
                break;
        }
    }

};
