#include "lists.h"

/**
*
*
*
*
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!*head)
		*head = new;
	else
	{
		while (curr->next)
		{
			if (number >= curr->n && number <= curr->next->n)
			{
				new->next = curr->next;
				curr->next = new;
				return (new);
			}
			else
				curr = curr->next;
		}
	}
	new->next = NULL;
	curr->next = new;
	return (new);
}
