#=======================================================
#단순 연결 리스트 (Singly Linked List)
#=======================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]"
#=======================================================
class SList:
    def __init__(self):
        self.head = None
        self.count = 0   #SList에 연결된 노드의 개수 (를 항상 유지한다.)
    #-----------------------------
    def __len__(self):
        return self.count
    #-----------------------------
    # 기존의 리스트 맨 뒤에 새 노드(newNode)를 연결한다.
    def insertFront(self, newNode):
        if self.head is None: #빈 리스트에 처음 추가하는 경우
            self.head = newNode
            self.count = 1
        else:   #1개 이상의 기존 노드가 있는 경우
            newNode.next = self.head
            self.head = newNode
            self.count += 1
    #-----------------------------
    def append(self,newNode):
        if self.head is None: # SList가 빈 리스트인 경우
            self.head = newNode # 추가하려는 새 노드(newNode)가 첫 노드가 된다.
            self.count = 1
        else:  # 1개 이상의 노드가 있는 경우, (마지막 노드를 찾아서 그 뒤에 newNode를 연결한다.)
            current = self.head # 리스트의 첫 노드(self.head)부터 순서대로 확인하며 마지막 노드를 찾는다.
            while current.next is not None: # 현재 노드(current)의 다음 노드가 있으면
                current = current.next  # current는 다음 노드를 가리키도록 설정하였다.
            # current.next가 None이면 while 종료, ==> current가 마지막 노드임을 의미
            # 새 노드(nowNode)를 current 뒤에 연결한다.
            current.next = newNode
            # 새 노드가 추가되었으므로 self.count 값 변경
            self.count += 1
    #-----------------------------
    # 리스트의 현재 연결 상황을 출력한다.
    # 빈리스트의 경우: [Empty]
    # 그 외의 경우: [100] -[200]-...-[300]-[None] 형식으로 출력 예정
    def showList(self):
        print("[Head]->", end="") # 초기 정보를 출력하고 줄바꿈 하지 않음. (->다음 이어질 출력과 연결)
        current = self.head       # 리스트의 첫 노드부터 차례대로 방문하며 노드 값을 출력하기

        while current is not None:
            print(f"[{current.data}]-", end="") #현재 노드(current)의 data를 출력.
            current = current.next

        print(f"||({self.count} nodes.)")
    #-------------------------------------
    def appendValue(self, value):
        self.append(Node(value))
    #-------------------------------------
    # 리스트의 첫 노드(head)를 삭제하며 반환한다. (빈 리스트이면 None 반환)
    def unshift(self):
        if self.head is None:
            return None
        else:
            header = self.head
            self.head = self.head.next
            header.next = None
            self.count -= 1
            return header
    #-------------------------------------
    # 리스트의 노드 연결 순서를 역순으로 재구성한다. (헤드가 마지막 노드로 변경된다.)
    def reverse(self):
        revList = SList() # 역순으로 재구성하는데 활용할 빈 리스트 생성.

        # 기존 리스트의 첫 노드를 차례대로 제거하며 revList에 insertFront()처리한다.
        while self.head is not None:
            h = self.unshift() # 기존 리스트의 첫 노드를 제거한다. (h에 저장)
            revList.insertFront(h) # 새 리스트(revList)의 insertFront()로 제거한 노드를 추가한다.
        
        #역순으로 재구성된 리스트의 정보를 현재 리스트로 옮겨온다.
        self.head = revList.head
        self.count = revList.count
    #-------------------------------------
    # 정렬되지 않은 현재의 리스트를 정렬 상태로 재구성한다.
    def sort(self, order="UP"):
        sorted = SList()  # 정렬된 노드를 담을 새로운 리스트
        #현재 리스트의 노드를 하나씩 차례대로 꺼내서 sorted 리스트에 insertSorted로 추가한다.
        while self.count:
            sorted.insertSorted(self.unshift(), order)

        self.head = sorted.head
        self.count = sorted.count
    #-------------------------------------
    # 현재 리스트의 복사본 리스트를 생성하여 반환하기
    def copy(self):
        newList = SList()  # 새로운 리스트를 만들기
        current = self.head  # 현재 리스트의 첫 노드부터 시작

        while current is not None:
            copy.appendValue(current.data)  # 노드의 데이터를 복사해서 새 노드로 추가
            current = current.next

        return newList  # 복사된 리스트 반환
    #-------------------------------------
    # 현재 단순 연결 리스트의 파이썬 리스트 버전을 생성하여 반환한다.
    def list(self):
        newList = List  # 새로운 리스트를 만들기
        current = self.head  # 현재 리스트의 첫 노드부터 시작

        while current:
            copy.append(current.data)  # 노드의 데이터를 복사해서 새 노드로 추가
            current = current.next

        return newList  # 복사된 리스트 반환
    #-------------------------------------
    #리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
    def insertSorted(self, newNode, order="UP"):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            # 새 노드(newNode)가 삽입될 위치를 찾기 위한 준비를 한다.
            current = self.head # 새 노드보다 큰 값을 가진 노드를 차례대로 찾아가기 위한 변수 (첫 노드부터 비교 시작)
            previous = None     # current가 다음 노드로 이동할 때, 현재의 current값을 백업하며 따라간다.
            
            while current is not None: #리스트의 마지막 노드까지 비교할 예정.
                if order == "UP":
                    check = newNode.data > current.data
                else:
                    check = newNode.data < current.data

                if check:
                    previous = current
                    current = current.next
                else:
                    if previous is None: # 첫 노드 앞에 추가되어야 하는 경우
                        newNode.next = current
                        self.head = newNode
                    else:
                        previous.next = newNode
                        newNode.next = current
                    self.count += 1
                    return
            # 리스트의 마지막에 새 노드를 연결해야 하는 경우
            previous.next = newNode
            self.count += 1


    #-------------------------------------
    # 특정값이 리스트 포함되어 있는지 결과를 알려주기
    # 반환값: 제거한 노드를 반환. 없으면 None
    def remove(self, value):
        targetNode = self.find(value)
        if targetNode is None:
            return None
        else:
            previous = None # current를 바로 이어서 따라가는 역활. 최종 삭제 작업에서 중요한 역활
            current = self.head
            while current is not targetNode:
                previous = current
                current = current.next
            
            # 이 지점에서는 current가 targetNode를 확인한 경우
            if previous is None:            # targetNode(current)가 리스트의 첫 노드이므로
                self.head = current.next    #리스트의  첫 노드(head)는 targetNode의 다음 노드가 된다.
            else:
                previous.next = current.next
            # 마무리 하고 반환값 설정
            current.next = None # 삭제 대상 노드의 연결 고리(next) 제거
            self.count -= 1
            return current

    #-------------------------------------
    #특정값이 리스트에 포함되어 있는지 결과를 알려주기
    # 반환값: 없을 경우 None, 있으면 해당 노드 반환.
    def find(self, value):
        current = self.head
        while current is not None:
            if value == current.data:
                return current
            else:
                current = current.next
        #Value를 찾지 못하면 while 종료
        return None
    

#=======================================================
slist = SList()
slist.appendValue(30)
slist.appendValue(130)
slist.appendValue(50)
slist.appendValue(40)
slist.appendValue(230)
slist.appendValue(10)
slist.showList()
newList = slist.copy()
slist.showList()
slist.unshift()
slist.showList()
newList.showList()
#=======================================================