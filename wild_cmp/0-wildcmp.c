#include "holberton.h"

/**
 * wildcmp - compare deux chaînes de caractére
 * où s2 peut contenir le caractère spécial '*'.
 * @s1: chaîne 1
 * @s2: chaîne 2
 *
 * Return: 1 si les chaîne sont identique, zero si ils ne le sont pas
 */

int wildcmp(char *s1, char *s2)
{
	if (*s1 == '\0' && *s2 == '\0')
		return (1);

	if (*s2 == '*')
	{
		if (*(s2 + 1) == '\0')
			return (1);
		if (wildcmp(s1, s2 + 1))
			return (1);
		if (*s1 != '\0' && wildcmp(s1 + 1, s2))
			return (1);
		return (0);
	}

	if (*s1 == *s2)
		return (wildcmp(s1 + 1, s2 + 1));

	return (0);
}
