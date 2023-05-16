// https://www.codewars.com/kata/53dc23c68a0c93699800041d
2023-03-17T21:27:52.960+0000
#include <stdlib.h>
#include <string.h>

char *smash (const char *const words[], size_t nb_words)
{
// allocate a string on the heap, memory will be freed
  //Initialise the string
  char *sentence = malloc(sizeof(char));
  sentence[0] = '\0';
  //Now we loop through the words
  for (size_t i = 0; i < nb_words; i++)  {
    sentence = realloc(sentence, strlen(sentence) + strlen(words[i]) + 2);
    strcat(sentence, words[i]);
    strcat(sentence, " ");
  }
  sentence[strlen(sentence) - 1] = '\0';
  
	return sentence;
}