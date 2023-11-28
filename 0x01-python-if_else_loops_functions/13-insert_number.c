#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *tail;

        tail = malloc(sizeof(listint_t));
        if (tail == NULL)
                return (NULL);
        tail->n = number;

        if (node == NULL || node->n >= number)
        {
                tail->next = node;
                *head = tail;
                return (tail);
        }

        while (node && node->next && node->next->n < number)
                node = node->next;

        tail->next = node->next;
        node->next = tail;

        return (tail);
}

