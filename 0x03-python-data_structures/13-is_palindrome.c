#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
    size_t length = sizeof(head) / sizeof(head[0]);

    if (*head == NULL) {
        return (1);
    }
    
    for (size_t i = 0; i < length; i++) {
        for (size_t j = length; j < length + 1; j--)
        {
            if (head[i] == head[j]) {
                return (1);
            }
        }
    }
    return (0);
}