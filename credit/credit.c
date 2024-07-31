#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void) {
    long cardNo = get_long("Number: ");

    // Convert the long integer to a string
    char card[20];  // Assuming a sufficiently large array for the string representation
    sprintf(card, "%ld", cardNo);

    // Implement Luhn's Algorithm to check validity
    int sum = 0;
    int length = 0;

    for (int i = strlen(card) - 1; i >= 0; i--) {
        int digit = card[i] - '0';

        if (length % 2 == 1) {
            digit *= 2;
            digit = digit / 10 + digit % 10;
        }

        sum += digit;
        length++;
    }

    bool isValid = (sum % 10 == 0);

    if (isValid){
        if (card[0] == "4" && strlen(card) >= 13 && strlen(card) <= 16){
            printf("VISA\n");
        }
        else if (card[0] == "3" && card[1] == "4" && strlen(card) == 15){
            printf("AMEX\n");
        }
        else if (card[0] == "5" && card[1] == "1" && strlen(card) == 16){
            printf("MASTERCARD\n");
        } else{
            printf("INVALID\n")
        }
    } else{
        printf("INVALID\n");
    }
    return 0;
}