// Using Array

#include <stdio.h>
#include <stdlib.h>


void print_email(int size, char* array[]) {
    for(int i = 0; i < size; i++) {
        printf("item at index %d: %s\n", i, array[i]);
    }

    printf("=========================================================\n");
}


void add_email(int size, char* array[]) {
    for(int i = 0; i < size; i++) {
        printf("add item to index %d: ", i);
        char email[100];
        scanf("%s", email);
        array[i] = email;
    }
    
    printf("=======================================================\n");
}


// Email Size
static int size = 2;

int main() {
   //char* email[] = {"paul@gmail.com", "offei@gmail.com"};
   char* email[size];

   add_email(size, email); 
   print_email(size, email);

    return 0;
}
