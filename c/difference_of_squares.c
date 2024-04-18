#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number) {
    // Using the formula n(n+1)(2n+1)/6
    return number * (number + 1) * (2 * number + 1) / 6;
}

unsigned int square_of_sum(unsigned int number) {
    // Using the formula n(n+1)/2
    unsigned int sum = number * (number + 1) / 2;
    return sum * sum;
}

unsigned int difference_of_squares(unsigned int number) {
    return square_of_sum(number) - sum_of_squares(number);
}
