#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to the head of the list.
 * @number: The number to insert.
 * 
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    /* Case 1: Insert at the beginning or into an empty list */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Case 2: Traverse the list to find the insertion point */
    current = *head;
    while (current->next != NULL && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
