#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list in which linkedList checked
 * Return: 0 if no cycle an 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if(!list)
		return 0;

	while(fast && slow && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if(slow == fast)
			return 1;

	}
	return 0;
}
