#include <stdio.h>
#define MAXLINE 1000 /* maximum input line length */
#define BELL '\007' /* define ascii octal number*/
#define BELL_H '\x07' /* define ascii hexadecimal number*/

void  Fahrenheit_Celsius_table();
void hello_word();
void print_info();
void character_input_output();
void Array();
// int power(int m, int n);
int power(int, int);
int get_line(char s[],int lim);
void print_longest_line();
void copy(char to[], char from[]);

int max = 30;
int min = 30;

int main() {
//    Fahrenheit_Celsius_table();
//    print_info();
//    Array();
//    printf("%d\n", power(3, 4));
//    print_longest_line();
//    int min; printf("min value:%d\n", min); // scope in function
//    extern int max; printf("extern max value:%d\n", max); //
    printf("octal value:%d\thex value:%d\t%d\n", 037, 0x37,BELL); // octal value:31  hex value:55
    return 0;
}

void print_info(){
    printf("%d\t%d\t%d\t%d\t%d\t%d\n", sizeof(char), sizeof(short), sizeof(int), sizeof(long), sizeof(float),sizeof(double)); // 1       2       4       8       4       8
//    printf("%d\t%d\n", sizeof(void), sizeof(sizeof));
    printf("%d\t\n", sizeof(void)); // L:long double , 0 is prefix respence octal, 0x means hexadecimal.
    float a= 1.0, b=1.01;
    printf("%6d\t%7d\t%6f\t%.2f\n", a, a, a, a); //  2  -295606400      1.000000        1.00
}

void hello_word(){
    printf("Hello, World!\n");
}

void Fahrenheit_Celsius_table(){
    int fahrenheit, celsius;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step =20;
    fahrenheit = lower;
    while (fahrenheit<=upper){
        celsius = 5 *(fahrenheit-32)/9;
        printf("%d\t%d\n", fahrenheit, celsius);
        fahrenheit = fahrenheit + step;
    }
}

void character_input_output(){
//     int c = getchar(); //get only one character
//     putchar(c);
//     printf("\n");
//     printf("%d\n",c);
//     while (c != EOF){ // linux:ctrl+d
//         c = getchar();
//         putchar(c);
//     }
    long nc; // character counting
    nc = 0;
    while (getchar()!= EOF) ++nc;
    printf("%ld\n", nc);

//    if(c == '\n') ++n1; // count line
//    if (c == ' ' || c == '\n' || c = '\t')

}

/* count digits, white space, others */
void Array(){
    int c, i, nwhite, nother;
    int ndigit[10];
    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;
    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9')
            ++ndigit[c-'0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;
    printf("digits =");
    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    printf(", white space = %d, other = %d\n",
           nwhite, nother);
}

/* power: raise base to n-th power; n >= 0 */
int power(int base, int n) {
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}

/* print the longest input line */
void print_longest_line() {
    int len;
    /* current line length */
    int max;
    /*
    maximum length seen so far */
    char line[MAXLINE];
    char longest[MAXLINE];
    /* current input line */
    /* longest line saved here */
    max = 0;
    while ((len = get_line(line, MAXLINE)) > 0)
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    if (max > 0) /* there was a line */
        printf("%s", longest);
    return 0;
}



/*  getline: read a line into s, return length */
int get_line(char s[],int lim) {
    int c, i;

    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

/* copy: copy 'from' into 'to'; assume to is big enough */
void copy(char to[], char from[])
{
    int i;
    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}

