#include <stdio.h>
#include <cstring>

int main() {

	int xint;
	float x = 10000000;

	memcpy(&xint, &x, sizeof(float));
	xint += 1;
	memcpy(&x, &xint, sizeof(float));

	printf("%.012f\n", x);

	return 0;

}
