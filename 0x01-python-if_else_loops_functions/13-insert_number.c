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

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	/* Consider when the number is smaller than the first node data */
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	/* Consider other posibilities */
	current = *head;
	/* Consider when the number is <  the first node data */
	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current)
	{
		/* Consider when even the last data is < number */
		if (number >= current->n && current->next == NULL)
			break;
		/* Insert the node at the expected position */
		if (current->n <= number && number <= current->next->n)
			break;
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
