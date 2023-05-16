// https://www.codewars.com/kata/57a0885cbb9944e24c00008e
// 2023-03-11T15:56:53.707+0000
#include <string.h>

// Write resulting string into buffer pointed by str_out
void remove_exclamation_marks(const char* str_in, char* str_out) {
	int count = 0;
	for (int i = 0; i < strlen(str_in); i++) {
		if (str_in[i] != '!') {
			str_out[count] = str_in[i];
			count++;
		}
	}
  
  str_out[count] = '\0';
}