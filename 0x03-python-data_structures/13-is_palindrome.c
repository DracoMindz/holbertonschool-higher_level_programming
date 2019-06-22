#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - check to see if linked lists are palindromes
 * @head: pointer to a pointer
 *
 * Return: 0 in false and 1 if true
 */
int is_palindrome(listint_t **head)
{
	int len, count, lencount;
	listint_t *nodePointer, *endPointer;

	if (head == NULL)
	{
		return (0);
	}
	if (*head == NULL)
	{
		return (1);
	}
	endPointer = *head;

	for (len = 0; endPointer != NULL; len++)
	{
		endPointer = endPointer->next;
		count = len;
	}
	nodePointer = *head;
	endPointer = *head;

	while (count > (len / 2))
	{
		endPointer = *head;
		lencount = 0;
		while (lencount < count)
		{
			endPointer = endPointer->next;
			lencount++;
		}
		if (nodePointer->n == endPointer->n)
		{
			nodePointer = nodePointer->next;
		}
		else
			return (0);
		count--;
	}
	return (1);
}
