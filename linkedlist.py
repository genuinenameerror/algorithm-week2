class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#first_node = Node(5) # 현재는 next 가 없이 하나의 노드만 있습니다. [5]
#second_node = Node(12) # [12] 를 들고 있는 노드를 만듭니다.
#first_node.next = second_node # 그리고, [5]의 next 를 [12]로 지정합니다. [5] -> [12]
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.
    def append(self, value):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head         
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다. 
            cur = cur.next          
        cur.next = Node(value)
    def print_all(self):
        cur = self.head
        if cur is not None:
            print("링크드 리스트 출력")
            print(cur.data,end=' ')        
        while cur.next is not None:            
            cur = cur.next
            print(cur.data,end=' ')
        print("")    
        print("더 이상 출력할 내용이 없습니다")
    def get_node(self, index):
        counter=0
        cur = self.head
        '''
        while cur is not None:
            if counter==index:
                return cur.data
            else:
                cur = cur.next
                counter+=1
        return 404
        '''
        while counter<index:
            cur = cur.next
            counter+=1
        return cur.data
    def add_node(self, index, value):
        counter=0
        cur=self.head
        if index==0:
            temp=self.head
            self.head = Node(value)
            self.head.next = temp            
            return              
        while counter<index-1:
            cur = cur.next
            counter+=1
        temp = cur.next
        cur.next=Node(value)
        cur = cur.next
        cur.next=temp
        #return "index 번째 Node 뒤에 value 를 추가하세요!"
    def delete_node(self, index):
        counter=0
        cur=self.head
        if index==0:
            self.head = cur.next
            return        
# index=2이면 counter가 1에서 끝남?
# 1까지 끊고 2를 잘라야 함 
        while counter<index-1:
            cur=cur.next
            counter+=1
        tail = cur.next
        tail=tail.next
        cur.next=tail
    def make_decimal(self):
        cur=self.head
        decimal = 0
        while cur is not None:
            decimal*=10
            decimal+=cur.data
            cur=cur.next
        return decimal
        
def get_linked_list_sum(linked_list_1, linked_list_2):
    '''
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end=' ')
            cur = cur.next
        print("")
'''
    # 구현해보세요!    
    return linked_list_1.make_decimal()+linked_list_2.make_decimal()

        
         
linked_list = LinkedList(5)
print(linked_list.head.data) # 5가 출력됩니다!
# 현재 LinkedList 는 (5) 만 존재합니다!

linked_list.append(12)
# 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
linked_list.append(8)
# 이렇게 되면 5 -> 12 -> 8 형태로 노드를 연결한 겁니다!
linked_list.append(33)
linked_list.print_all()
index = 0
print(index,"번 값은",linked_list.get_node(index) )
linked_list.print_all()
print("노드 추가")
linked_list.add_node(0, 99)
linked_list.print_all()
print("노드 추가")
linked_list.add_node(2, 44)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()
####################
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
linked_list_1.print_all()
print(linked_list_1.make_decimal())
print(get_linked_list_sum(linked_list_1, linked_list_2))
