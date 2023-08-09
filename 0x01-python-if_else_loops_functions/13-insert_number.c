#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: The pointer to the list head pointer
 * @number: The number to be inserted
 *
 * Return: A pointer to the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (*head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	current = *head;
	if (number < current->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current)
	{
		if (number > current->n && current->next == NULL)
		{
			new_node->next = NULL;
			current->next = new_node;
			return (new_node);
		}
		if (current->n < number && number < current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		if (number > current->n && current->next == NULL)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (NULL);
}
