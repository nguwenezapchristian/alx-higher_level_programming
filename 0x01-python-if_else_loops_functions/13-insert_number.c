#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to the firt pointer in node
 * @number: data of the inserted node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	int a = 0, n = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	current = *head;
	while ((current->n) < number)
	{
		current = current->next;
		n++;
	}
	current = *head;
	while ((current->n) < number)
	{
		if (a == (n - 1))
		{
			new->next = current->next;
			current->next = new;
		}
		current = current->next;
		a++;
	}
	return (new);
}
