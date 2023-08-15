#include "lists.h"

/**
 * add_node - adds a new node at the beginning of a listint_t list
 * @head: A pointer to a head pointer
 * @n: An integer to be included in node
 *
 * Return: A pointer to the new node or NULL if it fails
 */
listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: A pointer to the head pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *head1, *head2 = NULL, *head2_cpy;

	if (*head == NULL)
		return (1);
	/* Make a new list to look like the reverse of original list */
	head1 = *head;
	while (head1)
	{
		add_node(&head2, head1->n);
		head1 = head1->next;
	}
	/* Compare the data of the two lists */
	head2_cpy = head2;
	head1 = *head;
	while (head1 && head2)
	{
		if (head1->n != head2->n)
		{
			free_listint(head2);
			return (0);
		}
		head1 = head1->next;
		head2 = head2->next;
	}
	free_listint(head2_cpy);
	return (1);
}
