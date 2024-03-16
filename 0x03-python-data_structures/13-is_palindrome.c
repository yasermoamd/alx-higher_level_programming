#include "lists.h"

/**
 * reverse_listint - reverse a linked list
 * @head: double pointer to the frist node in the list
 *
 * Return: pointer to the first node in the new list
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	listint_t *first_half = *head;
	listint_t *second_half = reverse_listint(&slow);

	while (second_half != NULL)
	{
		if (first_half->data != second_half->data)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
