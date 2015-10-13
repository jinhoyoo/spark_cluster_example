#include <stdio.h>

int main(int argc, char *argv[])
{
	int count, s = 0;
    int i;
    count = argc;
    for (i = 1; i < argc; i++)
    {
		s += atoi(argv[i]);
    }

    printf("%d", s);
	return 0;
}
