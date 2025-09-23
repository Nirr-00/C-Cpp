from Queue import *
#======================================================================================
# 이진 트리 (Binary Tree)
#======================================================================================
class BTree:
    def __init__(self, value):
        self.key = value
        self.left = None    # 트리 노드 생성 초기에는 왼쪽, 오른쪽 자식 트리가 없으므로 None
        self.right = None
    #----------------------------------------------------------------------------------
    def __str__(self):  # "[100]"
        return f"[{self.key}]"
    #----------------------------------------------------------------------------------
    # 노드를 포함한 왼쪽과 오른쪽 자식 노드의 상황까지 함께 표현하는 문자열을 반환하기 (아래 내용 참조)
    def node(self): # print(nodeA) => "[B] <- [A] -> [C]", "[B] <- [A] -> [None]"
        r = ""
        # 왼쪽 자식 노드 문자열 정리
        if self.left:
            r += str(self.left)
        else:
            r += "[None]"
        # 자신과 좌우 연결 화살표 정리
        r += "<-" + str(self) + "->"
        # 오른쪽 자식 노드 문자열 정리
        if self.right:
            r += str(self.right)
        else:
            r += "[None]"
        # 완성된 문자열 반환하기
        return r
    #----------------------------------------------------------------------------------
    # 전위 순회 (preorder traversal)
    # 1. root 방문.(방문 => 출력)
    # 2. 왼쪽 자식 트리를 같은 방식으로 방문.
    # 3. 오른쪽 자식 트리를 같은 방식으로 방문
    def preOrder(self):
        print(self, " ", end="")
        if self.left:
            self.preOrder(self.left)
        if self.right:
            self.preOrder(self.right)
    #----------------------------------------------------------------------------------
    def inOrder(self):
        print(self, " ", end="")
        if self.left:
            self.preOrder(self.left)
        if self.right:
            self.preOrder(self.right)
    #----------------------------------------------------------------------------------
    def postOrder(self):
        if self.left:
            self.preOrder(self.left)
        if self.right:
            self.preOrder(self.right)
        print(self, " ", end="")
    #----------------------------------------------------------------------------------
    def levelOrder(self):
        queue = Queue() # 레벨 순회시 다음 방문할 노드들을 저장하고 저장된 순서대로 꺼내오기 위해
        queue.add(self)

        while not queue.isEmpty():
            node = queue.remove()
            print(node, " ", end="")
            if node.self:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
            print("")   # 출력 종료 후, 줄바꿈 처리용
    #----------------------------------------------------------------------------------
    # 주어진 이진 트리의 노드 수를 카운팅하여 반환. (재귀함수 활용하기)
    # (왼쪽 자식 트리의 개수 + 오른쪽 자식 트리의 개수 + 1 (root 자신))
    def nodeCount(self):
        count = 1   #self 자신 먼저 카운팅.
        if self.left:
            count += self.left.noceCount()
        if self.right:
            count += self.right.nodeCount()

        #print(f"{self}({count})")
        return count
    #----------------------------------------------------------------------------------
    # 트리의 높이(height)를 계산하여 반환하기 (재귀함수 활용)
    def height(self):
        if self.left is None and self.right is None:    #터미널 노드(terminal node)인 경우
            return
        if self.left is None:
            return self.right.height() + 1
        if self.right is None:
            return self.left.height() + 1
        return max(self.left.height(), self.right.height()) + 1
    #----------------------------------------------------------------------------------
    # 완전 이진 트리(Complete Binary Tree)
    def isComplete(self):
        queue = Queue()
        queue.add(self)
        danger = False # 이후에 자식이 없는 노드가 발견되면 True 설정예정.

        while not queue.isEmpty():
            node = queue.remove()

            if node.left:
                if danger:  # 현재 노드(node) 이전에 자식이 없었던(왼쪽, 오른쪽 무관) 노드가 발생했었는지를 확인.
                    return False
                queue.add(node.left)
            else:
                danger = True
            #-------------------------------------------------------------
            if node.right:
                if danger:
                    return False
                queue.add(node.right)
            else:
                danger = True
            # queue의 모든 노드를 방문하고 여기까지 오면 완전 이진 트리임
            return True
            #-------------------------------------------------------------
            # 완전 이진 트리를 리스트(배열)로 변환하기
            def toList(self):
                if not self.isComplete():
                    return None
                #----------------------------------------------------------
                lst = [None]
                queue = Queue()
                queue.add(self)
                
                while not queue.isEmpty():
                    node = queue.remove()
                    lst.append(node.key)
                    if node.left:
                        queue.add(node.left)
                    if node.right:
                        queue.add(node.right)

                return lst
#======================================================================================
class BSTree(BTree):
    # 이진 탐색 트리에 새 키값을 가진 노드를 추가한다.
    def insert(self, value):
        if value < self.key:
            if self.left:
                return self.left.inserrttt(value)
            else:
                self.left = BSTree(value)
                return 1
        elif value > self.key:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTree(value)
                return 1
        else:
            return 0
#======================================================================================
nodeA = BTree("A")
nodeB = BTree("B")
nodeC = BTree("C")
nodeD = BTree("D")
nodeE = BTree("E")
nodeF = BTree("F")
nodeG = BTree("G")
nodeH = BTree("H")
nodeA.left = nodeB
nodeA.right = nodeC
print(nodeB, nodeA, nodeC)
