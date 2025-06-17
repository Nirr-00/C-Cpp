#include <stdio.h>
#include "array.h"

int main() 
{
    ArrayListType list;
    array_init(&list);

    array_insert(&list, 0, 10);
    array_insert(&list, 1, 20);
    array_delete(&list, 0);

    for(int i = 0; i < list.size; i++)
    {
        printf("%d ", list.array[i]);
        printf("\n");
    }

    return 0;
}
