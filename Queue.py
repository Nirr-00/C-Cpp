#=====================================================
# 이중 연결 리스트를 이용하여 큐(queue) 구현하기
#=====================================================
from DList import *

class QueueUnderFlow(exception):
    pass
#=====================================================
class Queue(DList):
    #큐에 새 데이터(value)를 추가한다.
    def add(self, value):
        self.append(value)

    #--------------------------------------------------
    # 큐에서 맨 앞(가장 오래 전에 추가된 데이터) 에 있는 데이터를 꺼낸다.
    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty!!")
        else:
            returnValue = self.head.data
            super().remove(self.head)
            return returnValue
        