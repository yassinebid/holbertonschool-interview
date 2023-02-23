#include <stdlib.h>
#include <stdio.h>
#include "palindrome.h"

/**
 * @param n : unsigned long n
 * @return int 
 */


int is_palindrome(unsigned long n)
{
    unsigned long x = 0, r, temp;

    temp = n;
    while (n != 0)
    {
        r = n % 10;
        x = x * 10 + r;
        n = n / 10;
    }

    if (x == temp)
        return 1;
    else
        return 0;
}