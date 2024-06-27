#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct array
{
    void **st;
    int size;
    int top;
    int count;
} AST;

AST *createstack()
{
    AST *head;
    head = (AST *)malloc(sizeof(AST));
    if (head)
    {
        printf("Enter stack size:\n");
        scanf("%d", &head->size);
        head->st = (void **)calloc(head->size, sizeof(void *));
        if (head->st)
        {
            head->top = -1;
            head->count = 0;
        }
        else
        {
            free(head);
            return NULL;
        }
    }
    return head;
}

bool pushstack(AST *head, void *dpin)
{
    if (head->count == head->size)
    {
        return false;
    }
    (head->count)++;
    (head->top)++;
    head->st[head->top] = dpin;
    return true;
}

void *popstack(AST *head)
{
    void *dpout;
    if (head->count == 0)
        return NULL;
    else
    {
        dpout = head->st[head->top];
        head->count--;
        head->top--;
    }
    return dpout;
}

void *stacktop(AST *head)
{
    if (head->count == 0)
        return NULL;
    return (head->st[head->top]);
}

bool stackempty(AST *head)
{
    if (head->top == -1)
        return true;
    return false;
}

bool stackfull(AST *head)
{
    if (head->top == head->size - 1)
        return true;
    return false;
}

int stackcount(AST *head)
{
    return (head->count);
}

void displaystack(AST *head, void (*printdata)(void *))
{
    int i;
    if (head->top == -1)
        printf("Stack is empty");
    for (i = head->top; i >= 0; i--)
    {
        printdata(head->st[i]);
    }
}

bool destroystack(AST *head)
{
    if (head)
    {
        while(head->count)
        {
            free(head->st[head->top]);
            head->top--;
            head->count--;
        }
        free(head->st);
        free(head);
        return true;
    }
    return false;
}

// Creating a stack of students
typedef struct students
{
    char name[25], usn[11], dept[6];
    int roll_no, sem;
} STUD;

void printstud(void *st)
{
    STUD *temp;
    if (st)
    {
        temp = (STUD *)st;
        printf("\nStudent details:\n");
        printf("Name: %s\n", temp->name);
        printf("USN: %s\n", temp->usn);
        printf("Department: %s\n", temp->dept);
        printf("Roll number: %d\n", temp->roll_no);
        printf("Semester: %d\n", temp->sem);
    }
}

int main()
{
    STUD *s;
    AST *ph;
    int ch;

    // Initialize the stack
    ph = createstack();

    printf("\nStack of students using array stack ADT\n");
    while (1)
    {
        printf("\n1-Push a student, 2-Pop a student, 3-Student on the stack top, 4-Display students, 5-Stack empty, 6-Stack full, 7-Stack count, 8-Destroy stack\n");
        printf("Enter choice: ");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            s = (STUD *)malloc(sizeof(STUD));
            if (!s)
            {
                printf("Memory allocation failed\n");
                break;
            }
            printf("Enter student details:\n");
            printf("Name, USN, Department, Roll number, Semester\n");
            scanf("%s %s %s %d %d", s->name, s->usn, s->dept, &s->roll_no, &s->sem);
            if (pushstack(ph, s))
                printf("Successful\n");
            else
                printf("Failed\n");
            break;
        case 2:
            s = (STUD *)popstack(ph);
            if (s)
            {
                printf("Popped student details:\n");
                printstud(s);
                free(s); // Free the memory for the popped student
            }
            else
                printf("Stack is empty\n");
            break;
        case 3:
            s = (STUD *)stacktop(ph);
            if (s)
            {
                printf("Student on the stack top:\n");
                printstud(s);
            }
            else
                printf("Stack is empty\n");
            break;
        case 4:
            displaystack(ph, printstud);
            break;
        case 5:
            if (stackempty(ph))
                printf("Stack is empty\n");
            else
                printf("Stack is not empty\n");
            break;
        case 6:
            if (stackfull(ph))
                printf("Stack is full\n");
            else
                printf("Stack is not full\n");
            break;
        case 7:
            printf("Number of students: %d\n", stackcount(ph));
            break;
        case 8:
            if (destroystack(ph))
                printf("Successful\n");
            else
                printf("Failed\n");
            return 0;
        default:
            printf("Invalid choice\n");
        }
    }
    return 0;
}
