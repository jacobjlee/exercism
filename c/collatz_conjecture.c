#include "collatz_conjecture.h"

int steps(int start) {
    if (start < 1) {
        return ERROR_VALUE;
    }

    int step_count = 0;
    while (start != 1) {
        if (start % 2 == 0) {
            start /= 2;
        } else {
            start = 3 * start +1;
        }
        step_count++;
    }

    return step_count;
}
