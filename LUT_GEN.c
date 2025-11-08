#include <stdio.h>
#include <stdlib.h>

int main () {
    printf("Generating LUT :\n");
    for (int i = 0; i < 256; i++) {
        srand(i);
        printf("%d:%08x\n", i, rand());
    }
}