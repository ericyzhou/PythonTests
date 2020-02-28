# Node object
class Node:
    node_title = ""
    point_before = None
    point_after = None

    def __init__(self, title):
        self.node_title = title
        self.point_before = None
        self.point_after = None

    def get_node(self, title):
        if self.node_title == title:
            return self
        elif self.point_after is None:
            return None
        else:
            return self.point_after.get_node(title)


# Doubly Linked List
class DoublyLinkedList:
    list_head = None
    list_tail = None

    def __init__(self):
        self.list_head = None
        self.list_tail = None

    def insert_beginning(self, node):
        if self.list_head is None:
            self.list_head == node
            self.list_tail == node
        else:
            node.point_after = self.list_head
            self.list_head.point_before = node
            self.list_head = node

    def insert_end(self, node):
        if self.list_head is None:
            self.list_head = node
            self.list_tail = node
        else:
            node.point_before = self.list_tail
            self.list_tail.point_after = node
            self.list_tail = node

    def insert_before(self, node, title):
        x = self.list_head.get_node(title)
        if x is None:
            print("Node not found")
        else:
            if x.point_before is None:
                node.point_before = None
                node.point_after = x
                x.point_before = node
                self.list_head = node
            else:
                node.point_before = x.point_before
                x.point_before = node
                node.point_after = x
                node.point_before.point_after = node

    def insert_after(self, node, title):
        x = self.list_head.get_node(title)
        if x is None:
            print("Node not found")
        else:
            if x.point_after is None:
                x.point_after = node
                node.point_after = None
                node.point_before = x
                self.list_tail = node
            else:
                node.point_after = x.point_after
                x.point_after = node
                node.point_before = x
                node.point_after.point_before = node

    def remove_at(self, title):
        x = self.list_head.get_node(title)
        if x is None:
            print("Node not found")
        else:
            if x.point_before is None and x.point_after is None:
                self.list_head = None
                self.list_tail = None
            elif x.point_before is None:
                self.list_head = x.point_after
                x.point_after = None
            elif x.point_after is None:
                self.list_tail = x.point_before
                x.point_before = None
            else:
                x.point_before.point_after = x.point_after
                x.point_after.point_before = x.point_before
                x.point_before = None
                x.point_after = None

    def print_all(self):
        print_list(self.list_head)

    def print_pointers(self):
        print_everything(self.list_head)

    def print_head_tail(self):
        if self.list_head is None:
            print("Head is None", end="")
        else:
            print("Head is " + self.list_head.node_title, end="")

        if self.list_tail is None:
            print(", Tail is None")
        else:
            print(", Tail is " + self.list_tail.node_title)


# Print title helper
def print_list(node):
    if node is None:
        pass
    else:
        print(node.node_title)
        print_list(node.point_after)


# Print everything helper
def print_everything(node):
    if node is None:
        pass
    else:
        if node.point_before is None:
            print("Null", end='')
        else:
            print(node.point_before.node_title, end='')
        print(" <-- " + node.node_title + " --> ", end='')
        if node.point_after is None:
            print("Null")
        else:
            print(node.point_after.node_title)
        print_everything(node.point_after)


a = Node("Node 1")
b = Node("Node 2")
c = Node("Node 3")
d = Node("Node 4")
e = Node("Node 0")
f = Node("Node 2.5")
g = Node("Node 3.5")

double_list = DoublyLinkedList()
double_list.insert_end(a)
double_list.insert_end(b)
double_list.insert_end(c)
double_list.insert_end(d)

double_list.print_head_tail()
double_list.print_all()
double_list.print_pointers()

double_list.insert_beginning(e)
double_list.insert_before(f, "Node 3")
double_list.insert_after(g, "Node 3")

print("")
double_list.print_head_tail()
double_list.print_all()
double_list.print_pointers()

double_list.remove_at("Node 2.5")
double_list.remove_at("Node 3.5")

print("")
double_list.print_head_tail()
double_list.print_all()
double_list.print_pointers()
