#include <stdio.h>

int main(void)
{
    int height, length, width, volume, weight;
    printf("Enter height of box: ");
    scanf("%d", &height);
    printf("Enter length of box: ");
    scanf("%d", &length);
    printf("%d", width);
    scsnf("%d", width);

    volume = height * length * width;
    weight = (volume + 165) / 166;

    printf("Volume (cubic inches): %d", volume);
    printf("Dimensional weight (pounds): %d", weight);

    return 0;
}