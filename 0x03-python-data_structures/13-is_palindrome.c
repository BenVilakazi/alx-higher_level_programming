#include "lists.h"
/**
 * is_palindrome - funtion for check list
 * @head: pointer to head of linked list
 * Return: 1 if is true, else 0
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j;
	listint_t *aux = *head;
	int *datos = NULL;
	/* empty list is palindorme */
	if (head == NULL)
		return (1);
	/* length the single list linked */
	while (aux != NULL)
	{
		aux = aux->next;
		i++;
	}
	/* reset var and ponter for get data of linked list */
	aux = *head;
	datos = malloc(sizeof(int) + i);
	if (datos == NULL)
		return (0);

	i = 0;
	while (aux != NULL)
	{
		datos[i] = aux->n;
		aux = aux->next;
		i++;
	}
	for (j = 0; i > 0; j++)
	{
		i--;
		if (datos[j] != datos[i])
			return (0);

	}
	return (1);
}