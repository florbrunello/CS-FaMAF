#include <stdio.h>

int main(void) {
    int x = 3;
    int y = 10;
    y = *(&x);
    printf(y);
}

