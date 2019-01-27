#include <stdio.h>
int main() {
  long target = 600851475143;
  long last = -1;
  while (target % 2 == 0) {
    target /= 2;
    last = 2;
  }

  for (int i = 3; i <= target; i += 2) {
    if (target == 1) {
      break;
    }

    while (target % i == 0) {
      target /= i;
      last = i;
    }
  }

  printf("%ld\n", last);
}
