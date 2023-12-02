#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;
    int is_palindrome = 1;   
    if (*head == NULL || (*head)->next == NULL)
        return (1);
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }
    if (fast != NULL)
        slow = slow->next;
    while (prev != NULL)
    {
        if (prev->n != slow->n)
        {
            is_palindrome = 0;
            break;
        }
        prev = prev->next;
        slow = slow->next;
    }
    temp = NULL;
    prev = NULL;
    while (*head != NULL)
    {
        temp = (*head)->next;
        (*head)->next = prev;
        prev = *head;
        *head = temp;
    }
    *head = prev;    
    return (is_palindrome);
}
