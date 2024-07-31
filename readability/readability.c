#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string sentence);
int count_words(string sentence);
int count_sentences(string sentence);

int main(void){
    string sent = get_string("Text: ");

    int letters = count_letters(sent);
    int words = count_words(sent);
    int sentences = count_sentences(sent);

    //printf("Letter Count = %d, Words Count = %d, Sentence Count = %d\n", letters, words, sentences);

    //index = 0.0588 * (avg no of letters per 100 words) - 0.296 * (avg no of sentences per 100 words) - 15.8
    float L = (float)(((float)letters / (float)words) * 100);
    float S = (float)(((float)sentences / (float)words) * 100);

    //printf("L: %f, S: %f\n", (float)L, S);

    float index = (L * 0.0588) - (S * 0.296) - 15.8;
    index = (int)round(index);

    //printf("%.0f\n", index);

    if (index < 1){
        printf("Before Grade 1\n");
    } else if (index >= 1 && index <= 16){
        printf("Grade %.0f\n", index);
    } else if (index > 16){
        printf("Grade 16+\n");
    }
}

int count_letters(string sentence){
    int letterCount = 0;
    for (int i = 0; i < strlen(sentence); i++){
        if (isalpha(sentence[i])){
            letterCount++;
        }
    }
    return letterCount;
}

int count_words(string sentence){
    int wordCount = 0;
    for (int j = 0; j < strlen(sentence); j++){
        if (sentence[j] == ' '){
            wordCount++;
        } else if (sentence[j] == ',' || sentence[j] == '.' || sentence[j] == '!' || sentence[j] == '?'){
            wordCount++;
            j++;
        }
    }
    if (wordCount == 0){
        wordCount = 1;
    }
    return wordCount;
}

int count_sentences(string sentence){
    int sentenceCount = 0;
    for (int k = 0; k < strlen(sentence); k++){
        if (sentence[k] == '.'|| sentence[k] == '!' || sentence[k] == '?'){
            sentenceCount++;
            k++;
        }
    }
    if (sentenceCount == 0){
        sentenceCount = 1;
    }
    return sentenceCount;
}