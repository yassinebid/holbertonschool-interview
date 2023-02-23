#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	unsigned int count = 0, i = 0;
	int list[99999];

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);
	while (tmp)
	{
		tmp = tmp->next;
		count = count + 1;
	}
	if (count == 1)
		return (1);

	tmp = *head;
	while (tmp)
	{
		list[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; i <= count / 2; i++)
	{
		if (list[i] != list[count - i - 1])
			return (0);
	}
	return (1);
}
