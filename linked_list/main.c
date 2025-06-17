#include <stdio.h>
#include "linked_list.h" // 헤더파일 이름에 맞게 include

int main() 
{
    Node* head = NULL; // 연결 리스트의 시작점(헤드) 선언 및 초기화

    // 노드 추가
    append_node(&head, 10);    // 맨 뒤에 10 추가
    append_node(&head, 20);    // 맨 뒤에 20 추가
    insert_node(&head, 1, 15); // 1번 위치(두 번째)에 15 삽입

    printf("리스트 출력: ");
    print_list(head); // 현재 리스트 상태 출력

    // 노드 삭제
    delete_node(&head, 1); // 1번 위치(두 번째) 노드 삭제

    printf("삭제 후 리스트 출력: ");
    print_list(head);

    // 모든 노드 메모리 해제
    free_list(head);

    return 0;
}
