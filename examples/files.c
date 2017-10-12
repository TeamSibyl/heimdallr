#include <stdio.h>

void writeFile(const char* s)
{
  FILE *fp;

  fp = fopen("test.txt", "w+");
  fprintf(fp, "%s\n",s);
  fclose(fp);
}

int main() {
   writeFile("Blargh");
}
