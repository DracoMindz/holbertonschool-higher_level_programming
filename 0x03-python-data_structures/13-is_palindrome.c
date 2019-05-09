#ifndef LISTS_H
#define LISTS_H

/**
 * is_palindrome - check to see if linked lists are palindromes
 * @head: pointer to a pointer
 *
 * Return: 0 in false and 1 if true
 */
int is_palindrome(listint_t **head)
{
	int len, count;
	listint_t *nodePointer, *endPointer;

	if (head == NULL || *head == NULL)
	{
		return (NULL);
	}
	endPointer = *head;

	for (len = 0; endPointer != NULL; len++)
	{
		endPointer = endPointer->next;
		count = len;
	}
	nodePointer = *head;
	endPointer = *head;

	while ((count/2) > 0)
	{
		if (nodePointer->n == endPointer->n)
		{
			nodePointer = nodePointer->next;
			{
				while (len > 0)
				{
					endPointer = endPionter->next;
				}
		else:
			return (0);
	        len--;
			}
		}
	}
		nodePointer = *head;
		endpointer = *head;
		return (1);
}
