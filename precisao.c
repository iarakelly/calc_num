#include <stdio.h>
#include <stdlib.h>

int main() {

	float soma = 0;
	float delta = 0.2;
	int n = 10000;

	for(int i = 0; i < n; i++) {
		soma += delta;
	}

	printf("%f = %f?\n", delta*n, soma);

	return 0;
}
