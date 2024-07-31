#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

int main(void) {
    int change = 0;
    int numOfCoins = 0;

    do{
        change = get_int("Change owed: ");

        if (change >= 25) {
            numOfCoins += change / 25;
            change %= 25;
        }
        if (change >= 10) {
            numOfCoins += change / 10;
            change %= 10;
        }
        if (change >= 5) {
            numOfCoins += change / 5;
            change %= 5;
        }
        if (change >= 1) {
            numOfCoins += change / 1;
            change %= 1;
        }
    }
    while (change < 0);

    printf("%d\n", numOfCoins);

}
