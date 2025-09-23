"""
    이중 연결 리스트(Double Linked List)
"""
#==========================================================
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"[{self.data}]"
#==========================================================
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #-----------------------------------------------------
    # 리스트의 맨 뒤에 VALUE값을 가진 새 노드를 연결한다.
    def append(self, value):
         # 새로 추가할 노드 생성
        newNode = Node(value)
        # 빈 리스트인 경우를 먼저 확인하고 처리한다.
        if self.count == 0:
             self.head = newNode
             self.tail = newNode
        else: # 빈 리스트가 아닌경우
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    # 리스트의 노드 개수 증가 반영
        self.count += 1
    #-----------------------------------------------------
    # 리스트의 맨 앞에서 value값을 가진 새 노드를 추가한다.
    def insertFront(self, value):
        if self.count == 0: # 빈 리스트인 경우
            self.append(value)
        else: # 빈 리스트가 아닌 경우
            # 새로 추가할 노드를 먼저 생성한다.
            newNode = Node(value)
            # 새로 생성한 노드를 리스트의 맨 앞에 추가한다.
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            # 리스트의 노드 개수 속성값 갱신.
            self.count += 1
    #-----------------------------------------------------
    # 리스트에서 value값을 가진 첫 노드를 찾아서 반환한다.
    # 없으면 None 반환.
    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None
    #-----------------------------------------------------
    def showList(self):
        print("head ->", end="")
        # head부터 마지막 노드까지 차례대로 노드를 출력한다.
        current = self.head
        while current:
            print(f"{current} ->", end="")
            current = current.next
        # 리스트의 노드 개수를 출력
        print(f"({self.count}개의 노드)")
    #-----------------------------------------------------
    # 리스트의 존재하는 targetNode앞에 value값을 가진 새 노드를 생성하여 삽입한다.
    def insertBefore(self, targetNode, value):
        if targetNode is None:
            return
        if targetNode is self.head:
            self.insertFront(value)
        else:
            newNode = Node(value)
            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode
            self.count += 1
    #-----------------------------------------------------
    # 리스트의 존재하는 targetNode뒤에 value값을 가진 새 노드를 생성하여 삽입한다.
    def insertAfter(self, targetNode, value):
        if targetNode is None:
            return
        if targetNode is self.tail:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = targetNode.next
            newNode.prev = targetNode
            targetNode.next.prev = newNode
            targetNode.next = newNode
            self.count += 1
    #-----------------------------------------------------
    # 현재 리스트(정렬되어 있는것으로 간주) 상태를 유지하면서 새 값(value)을 가진 노드를 추가한다.
    # 같은 값을 가진 노드가 이미 있으면 그 노드 앞에 추가한다.
    # 반환값: 없음
    def insertSorted(self, value):
        # value보다 크거나 값은 값을 찾아 그 앞에 Node(value)를 삽입한다.
        current = self.head
        while current is not None:
            if current.data > value: # Node(value)를 current 앞에 삽입한다
                self.insertBefore(current, value)
                return
            else:
                current = current.next
        # 빈 리스트이거나 추가하려는 값이 기존 모든 노드들의 값보다 큰 경우 다음 코드가 실행된다.
        self.append(value)
    #-----------------------------------------------------------------
    # 리스트에서 지정된 노드(targetNode)를 삭제한다. (연결구조에서 배제한다.)
    # 반환값: 없음.
    def remove(self, targetNode):
        if targetNode is None:
            return
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
        elif self.head is targetNode:
            self.head = targetNode.next
            targetNode.next.prev = None
        elif self.tail is targetNode:
            self.tail = targetNode.prev
            targetNode.prev.next = None
        else:
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev
        self.count -= 1
        del targetNode
#-----------------------------------------------------------------
        def isEmpty(self):
            if self.count == 0:
                return True
            return False