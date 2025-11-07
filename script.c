#include <stdio.h>
#include <stdlib.h>

int main () {
    // We'll create a LUT (Look Up Table): Key -> Value
    // Key : 0->255
    // Value : pseudo-random byte derived from rand() seeded by key
    printf("Generating LUT :\n");
    for (int i = 0; i < 256; i++) {
        srand(i);
        printf("%d:%08x\n", i, rand());
    }
}