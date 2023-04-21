#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *next;
}node;

void printlist(node * list){
    int n=0;
    printf("The resulting list is: ");
    while(list!=NULL){
        printf("%d ",list->data);
        list=list->next;
    }
    printf("\n");
}
node* readList(){
    int temp;//temp to save input, k is the length
    node *head=NULL,*last=NULL;
    printf("Enter list\n");
    while(scanf("%d",&temp)==1){
        node* n = (node *) malloc(sizeof(node));
        n->data=temp;
        if(head==NULL) {
            head=n;
            last = head;
        }else{
            last->next=n;
            last=last->next;
        }
        if(getchar()=='\n') break;
    }
    return head;
}

void q1(node* list){
    node* nxt=list->next,*nxtnxt;
    list->next=NULL;
    while(nxt!=NULL){
        nxtnxt=nxt->next;
        nxt->next=list;
        list=nxt;
        nxt=nxtnxt;
    }
    printlist(list);
}

void q2(node* list){
int x=1;
node *current=list,*middle=list;
while (current->next!=NULL)
{
    current=current->next;
    if(x++%2==0) middle=middle->next;
}
printf("The middle is: %d\n",middle->data);
}



void makeLoopForq3(node *list){
    node *last=list;
    while (last->next!=NULL)last=last->next;
    last->next=list;
}

int q3helper(node *list){
    node *advance1=list,*advance2=list;
    while (advance2!=NULL)
    {
        if(advance2->next==NULL) return 0;
        advance1=advance1->next;
        advance2=advance2->next->next;
        if(advance1==advance2) return 1;
    }
    return 0;
}

void q3(node *list){
    int x;
    printf("do you want it to contain a loop?(answer with 1 for yes and 0 for no)");
    scanf("%d",&x);
    if(x) makeLoopForq3(list);

    x=q3helper(list);
    if(x==0) printf("The list doesn't have a loop\n");
    if(x==1) printf("The list has a loop\n");
    
}


int main(){
    int q;
    node* list=readList();

    if(list==NULL) {
        printf("List is empty\n");
        return 0;
    }

    printf("Enter question number\n");
    scanf("%d",&q);

    switch (q)
    {
    case 1:
        q1(list);
        break;
    case 2:
        q2(list);
        break;
    case 3:
        q3(list);
        break;
    default:
        printf("Invalid input\n");
        break;
    }
    return 1;
}