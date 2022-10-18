class Node:
    def __init__(self,v):
        self.val = v
        self.next= None

class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_postition(self,pos,val):
        pass

    def insert_at_tail(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next=newNode

    def print_list(self):
        tmp = self.head
        while tmp!= None:
            print(tmp.val)
            tmp=tmp.next

def main():
    lst = Linked_list()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.print_list()
    # a = Node(10)
    # b = Node(23)
    # c = Node(30)

    # a.next = b
    # b.next = c




main()