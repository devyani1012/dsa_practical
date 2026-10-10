class node:
    def __init__(self, values):
        self.data = values
        self.next = None

class solution:
    def __init__(self):
        self.head = None

    def create_list(self, values):
        for value in values:
            new_node = node(value)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node


    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node

        else:
            p = 1
            temp = self.head

            while p < pos - 1 and temp is not None:
                temp = temp.next
                p += 1

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def middle_node(self):
            slow=self.head
            fast=self.head    
    
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
    
            if slow:
                print("middle node:",slow.data)    
            else:
                print("list is empty")          

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None") 

    def delete(self,value) :
        temp=self.head
        prev=None

        if temp.data==value:
            self.head=self.head.next
        else:
            while(temp.data!=value):
                prev=temp
                temp=temp.next
            if temp==None:
                    print("value is not present")
                    return
            prev.next=temp.next
            temp.next=None  
    def reverse(self):
        prev=None
        curr=self.head

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev 

    def sum_consecutive(self):
        temp=self.head

        while temp and temp.next:
            total=temp.data + temp.next.data
            print(total,end="->")
            temp=temp.next    




    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
list1 = solution()


list1.create_list([10,20,30,40,50,60])

print("linked list:")
list1.traverse()

list1.insert(node(54), 1)
print("After inserting at position 1:")
list1.print()


list1.middle_node()




list1.delete(50)

print("after delete:")
list1.print()

list1.reverse()
print("reversed node:")
list1.print()

print("list after consecutive")
list1.sum_consecutive()
