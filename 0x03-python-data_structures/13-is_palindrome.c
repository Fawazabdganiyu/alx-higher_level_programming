#include "lists.h"
#include <stdio.h>
/**
 * reverse_list - reverses a listint_t list
 * @head: A pointer to a head node
 *
 * Return: A pointer to the head of the reversed node
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *next;

	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: A pointer to the head pointer
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first_half, *second_half, *mid, *second_half_copy;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* Get the middle of the list */
	slow = *head;
	fast = *head;
	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	mid = slow;
	first_half = *head;
	second_half = reverse_list(slow->next);
	second_half_copy = second_half;
	/* Compare the first and second half data */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);

		first_half = first_half->next;
		second_half = second_half->next;
	}

	/* Reconnect the list */
	second_half = reverse_list(second_half_copy);
	mid->next = second_half;

	return (1);
}
