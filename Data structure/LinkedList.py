"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1

    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1
        return pop_data

    def first(self):
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data

    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next
        return self.current.data

    def size(self):
        return self.num_of_data


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print("first :", l_list.first())  # first : 5
    print("next :", l_list.next())  # next : 2
    print("size :", l_list.size())  # size : 7
    print("delete :", l_list.delete())  # delete : 2
    print("size :", l_list.size())  # size : 6
    print("current:", l_list.current.data)  # current: 5
    print("tail:", l_list.tail.data)  # tail: 11
    print("first :", l_list.first())  # first : 5
    print("next :", l_list.next())  # next : 1
    print("next :", l_list.next())  # next : 2
    print("next :", l_list.next())  # next : 7

    # 전체 노드 data 표시하기
    data = l_list.first()

    if data:
        print(data, end=" ")
        while True:
            data = l_list.next()
            if data:
                print(data, end=" ")
            else:
                break
    # 5 1 2 7 2 11


    # 2만 삭제하기
    data = l_list.first()

    if data and data == 2:
        l_list.delete()
        print("deleted", end=" ")
    else:
        print(data, end=" ")

    while True:
        data = l_list.next()
        if data == 2:
            l_list.delete()
            print("deleted", end=" ")
        elif data:
            print(data, end=" ")
        else:
            break
"""
"""
class Node:
    def __init__(self, data):
        self.current = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
 


    def add(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        else:
             
            self.current.next = new_Node
        

    def delete(self,data)

    def find(self, data)

    def print(self)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def add_front(self, data):
        new_Node = Node(data)
        if self.is_empty():
            self.head = new_Node
        else:
            new_Node.link = self.head
            self.head = new_Node

        self.count += 1

    def add_last(self, data):
        new_Node = Node(data)
        if self.is_empty():
            self.head = new_Node
        else:
            cur = self.head
            while cur.link is not None:
                cur = cur.link
            cur.link = new_Node
        self.count += 1

    def delete(self, item):
        if self.is_empty():
            return None
        elif self.head.data == item:
            self.delete_front()
            return True
        else:
            cur = self.head
            while cur.link is not None:
                if cur.data == item:
                    self.delete_item(item)

                    self.count -= 1
                    return True
                cur = cur.link

        return False

    def delete_item(self, item):

        cur = self.head
        while cur.link is not None:
            if cur.link == item:
                nextnode = cur.link.link
                cur.link = nextnode
                self.count -= 1
                break

    def delete_front(self):
        if self.is_empty():
            return None
        else:
            self.head = self.head.link
            self.count -= 1

    """
    def add_after(self,data, index):
        new_Node = Node(data)
        if self.is_empty():
            self.head = new_Node
        else:
            
        self.count += 1
    def delete_after(self, data, index):
        self.count -= 1
    """

    def search(self, item):
        cur = self.head
        cnt = 0
        while cur.link is not None:
            if cur.data == item:
                return cnt
            cnt += 1
        return None

    def print_list(self):

        cur = self.head
        while cur.link is not None:
            print(str(cur.data), end=", ")
            cur = cur.link


a = LinkedList()
a.add_last(7)
a.add_front(3)
a.add_front(4)
a.add_last(5)
a.add_last(7)
a.add_last(7)
a.delete(5)

a.print_list()

# print(a.search(4))
