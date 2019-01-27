#include <stdio.h>
int main()
{
  int sum = 0;
  for (int i = 3; i < 1000; i += 3) {
    sum += i;
  }

  for (int i = 5; i < 1000; i += 5) {
    if (i % 3 != 0) {
      sum += i;
    }
  }

  printf("%d\n", sum);
  return 0;
}
