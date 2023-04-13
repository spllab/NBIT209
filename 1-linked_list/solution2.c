// Using Link Representation

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char* email;
    struct node* next;
}Node;


void print_email(Node* head) {
    while(head != NULL) {
        printf("%s\n", head->email);
        head = head->next;
    }
    printf("===========================================\n");
}



int main() {
//    Node offei = {"offei@gmail.com", NULL};
//    Node paul = {"paul@gmail.com", &offei};
//    Node* head = &paul;
   
   //printf("%s %s %p\n", paul.email, paul.next->email, paul.next->next);
   //printf("%s %s %p\n", head->email, head->next->email, head->next->next);
   //print_email(head);

   

    return 0;
}
