#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

// 새로운 노드를 생성하는 함수
Node* create_node(int data) 
{
    Node* new_node = (Node*)malloc(sizeof(Node)); // 메모리 동적 할당
    new_node->data = data;      // 데이터 저장
    new_node->next = NULL;      // 다음 노드 포인터 NULL로 초기화
    return new_node;            // 생성된 노드 반환
}

// 연결 리스트의 맨 끝에 노드를 추가하는 함수
void append_node(Node** head, int data) 
{
    Node* new_node = create_node(data); // 새로운 노드 생성
    if (*head == NULL) {                 // 리스트가 비어있는 경우
        *head = new_node;                // 새로운 노드를 헤드로 설정
        return;
    }
    
    Node* current = *head;               // 현재 노드를 헤드로 초기화
    while (current->next != NULL) {      // 리스트의 끝까지 이동
        current = current->next;
    }
    current->next = new_node;            // 마지막 노드의 next를 새로운 노드로 설정
}

// 원하는 위치에 노드를 삽입하는 함수
void insert_node(Node** head, int position, int data) 
{
    Node* new_node = create_node(data); // 새로운 노드 생성
    if (position == 0) {                 // 리스트의 맨 앞에 삽입하는 경우
        new_node->next = *head;          // 새로운 노드의 next를 현재 헤드로 설정
        *head = new_node;                // 헤드를 새로운 노드로 업데이트
        return;
    }
    
    Node* current = *head;               // 현재 노드를 헤드로 초기화
    for (int i = 0; i < position - 1 && current != NULL; i++) {
        current = current->next;         // 원하는 위치까지 이동
    }
    
    if (current == NULL) {               // 위치가 리스트의 길이를 초과한 경우
        printf("Position out of bounds.\n");
        free(new_node);                  // 메모리 해제
        return;
    }
    
    new_node->next = current->next;      // 새로운 노드의 next를 현재 노드의 next로 설정
    current->next = new_node;            // 현재 노드의 next를 새로운 노드로 설정
}

// 원하는 위치의 노드를 삭제하는 함수
void delete_node(Node** head, int position) 
{
    if (*head == NULL) {                 // 리스트가 비어있는 경우
        printf("List is empty.\n");
        return;
    }
    
    Node* current = *head;               // 현재 노드를 헤드로 초기화
    if (position == 0) {                 // 리스트의 맨 앞 노드를 삭제하는 경우
        *head = current->next;           // 헤드를 다음 노드로 업데이트
        free(current);                   // 메모리 해제
        return;
    }
    
    for (int i = 0; i < position - 1 && current != NULL; i++) {
        current = current->next;         // 원하는 위치까지 이동
    }
    
    if (current == NULL || current->next == NULL) { // 위치가 리스트의 길이를 초과한 경우
        printf("Position out of bounds.\n");
        return;
    }
    
    Node* temp = current->next;          // 삭제할 노드를 임시 변수에 저장
    current->next = temp->next;          // 현재 노드의 next를 삭제할 노드의 next로 설정
    free(temp);                          // 메모리 해제
}

// 연결 리스트 전체를 출력하는 함수
void print_list(Node* head) 
{
    Node* current = head;                // 현재 노드를 헤드로 초기화
    while (current != NULL) {            // 리스트의 끝까지 반복
        printf("%d -> ", current->data); // 현재 노드의 데이터 출력
        current = current->next;          // 다음 노드로 이동
    }
    printf("NULL\n");                     // 리스트의 끝을 표시
}

// 연결 리스트의 모든 노드를 메모리에서 해제하는 함수
void free_list(Node* head) 
{
    Node* current = head;                // 현재 노드를 헤드로 초기화
    Node* next_node;                      // 다음 노드를 저장할 변수
    while (current != NULL) {             // 리스트의 끝까지 반복
        next_node = current->next;        // 다음 노드 저장
        free(current);                    // 현재 노드 메모리 해제
        current = next_node;              // 다음 노드로 이동
    }
}