#include <stdio.h>
#include <cs50.h>

int main(void) {
    int number = get_int("Height: ");

    for (int i = 0; i < number; i++) {
        // Print leading spaces
        for (int j = 0; j < number - i - 1; j++) {
            printf(" ");
        }

        // Print hash symbols
        for (int j = 0; j <= i; j++) {
            printf("#");
        }

        printf("\n");
    }

    return 0;
}