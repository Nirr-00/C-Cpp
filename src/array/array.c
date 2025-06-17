#define MAX_LIST_SIZE 100

typedef int element;

typedef struct 
{
    element array[MAX_LIST_SIZE];
    int size;
} ArrayListType;

// 리스트 초기화
void array_init(ArrayListType *list)
{
    list->size = 0;
}

// 리스트가 비었는지 확인
int array_empty(ArrayListType *list)
{
    return list->size == 0; // 리스트가 비었을 때 1, 그렇지 않으면 0 반환
}

// 리스트가 가득 찼는지 확인
int array_full(ArrayListType *list)
{
    return list->size == MAX_LIST_SIZE; // 리스트가 가득 찼을 때 1, 그렇지 않으면 0 반환
}

// 특정 위치에 요소 삽입
void array_insert(ArrayListType *list, int position, element item)
{
    if(array_full(list) || position < 0 || position > list->size) 
    {
        return; // 리스트가 가득 찼거나 위치가 잘못되었을 때
    }

    for(int i = list->size; i > position; i--) 
    {
        list->array[i] = list->array[i - 1]; // 요소 이동
    }

    list->array[position] = item; // 새 요소 삽입

    list->size++; // 크기 증가
}

// 특정 위치 요소 삭제
void array_delete(ArrayListType *list, int position)
{
    if(array_empty(list) || position < 0 || position >= list->size) 
    {
        return; // 리스트가 비었거나 위치가 잘못되었을 때
    }

    for(int i = position; i < list->size - 1; i++) 
    {
        list->array[i] = list->array[i + 1]; // 요소 이동
    }

    list->size--; // 크기 감소
}