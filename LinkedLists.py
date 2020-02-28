class node:
    node_title = ""
    point_after = None

    def __init__(self, title):
        self.node_title = title
        self.point_after = None

    def point_to(self, item):
        if self.point_after is None:
            self.point_after = item
        else:
            self.point_after.point_to(item)

    def print_me(self):
        if self.point_after is None:
            print("I am " + self.node_title + ". I am pointing to nothing.")
        else:
            print("I am " + self.node_title +
                  ". I am pointing to " + self.point_after.node_title)
            self.point_after.print_me()


class NodeList:
    list_head = None

    def __init__(self):
        self.list_head = None

    def add_node(self, item):
        if self.list_head is None:
            self.list_head = item
        else:
            self.list_head.point_to(item)

    def print_all_nodes(self):
        if self.list_head is None:
            print("Empty")
        else:
            self.list_head.print_me()

    def pop(self):
        if self.list_head is None:
            pass
        else:
            print("Popped " + self.list_head.node_title)
            self.list_head = self.list_head.point_after


l = NodeList()

for x in range(1, 12):
    l.add_node(node(str(x)))

l.print_all_nodes()

l.pop()
l.print_all_nodes()
