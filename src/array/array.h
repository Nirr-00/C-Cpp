#ifndef ARRAY_H
#define ARRAY_H

#define MAX_LIST_SIZE 100

typedef int element;

typedef struct 
{
    element array[MAX_LIST_SIZE];
    int size;
} ArrayListType;

// 함수 선언부
void array_init(ArrayListType *list);
int array_empty(ArrayListType *list);
int array_full(ArrayListType *list);
void array_insert(ArrayListType *list, int position, element item);
void array_delete(ArrayListType *list, int position);

#endif
