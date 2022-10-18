from operator import ne


class Node:
    def __init__(self,v):
        self.val = v
        self.next= None

class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_pos(self,pos,val):
        newNode = Node(val)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            tmp = self.head
            for i in range(pos-1):
                tmp = tmp.next
                if tmp == None:
                  print("Out of Bound")
                  return  
            newNode.next = tmp.next
            tmp.next = newNode


    def insert_at_tail(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next=newNode
    def delete_at_pos(self,pos):
        if pos==0:
            delNode = self.head
            self.head = self.head.next
            del delNode
        else:
            tmp = self.head
            for i in range(pos-1):
                tmp = tmp.next
                if tmp == None:
                  print("Out of Bound")
                  return
            
            delNode = tmp.next
            if tmp.next == None:
                  print("Out of Bound")
                  return
            tmp.next = tmp.next.next
            del delNode 


    def print_list(self):
        tmp = self.head
        while tmp!= None:
            print(tmp.val)
            tmp=tmp.next
    def reverse_recursive(self):
        if self.head.next == None:
            return self.head
        save = self.head
        self.head = self.head.next
        newHead = self.reverse_recursive()
        save.next.next = save
        save.next = None
        return newHead

def main():
    lst = Linked_list()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    # lst.print_list()
    lst.insert_at_pos(1,100)
    lst.delete_at_pos(0)
    # lst.insert_at_pos(2,200)
    # lst.delete_at_pos(4)
    lst.head = lst.reverse_recursive()
    lst.print_list()

    # a = Node(10)
    # b = Node(23)
    # c = Node(30)

    # a.next = b
    # b.next = c




main()