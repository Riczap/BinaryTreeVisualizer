class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)

class Tree:
    def __init__(self, head=None):
        if type(head) == type(1):
            self.head = Node(head)
        elif type(head) == type(Node):
            self.head = head
        else:
            self.head = head
    
    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        tmp = self.head
        while True:
            if node.value <= tmp.value:
                if not tmp.left:
                    tmp.left = node
                    break
                else:
                    tmp = tmp.left
            else:
                if not tmp.right:
                    tmp.right = node
                    break
                else:
                    tmp = tmp.right
    def search(self, value):
        tmp = self.head
        parent = None
        direction = None
        while tmp:
            if tmp.value == value:
                return {'node': tmp,'parent': parent, 'direction': direction}
            elif tmp.value < value:
                parent = tmp
                direction = 'right'
                tmp = tmp.right 
            else:
                parent = tmp
                direction = 'left'
                tmp = tmp.left
        print(f'Value {value} not found')

    def search_rec(self, value):
        current_node = self.head
        if current_node.value == value:
            return current_node
        else:
            if current_node.value < value:
                current_tree = Tree(current_node.right)
                return current_tree.search(value)
            else:
                current_tree = Tree(current_node.left)
                return current_tree.search(value)

    def delete(self, value):
        target_node = self.search(value)['node']
        parent_node = self.search(value)['parent']
        direction = self.search(value)['direction']


        if target_node.value == self.head.value:
            if not self.head.left and not self.head.right:
                self.head = None
            new_tree = Tree(self.head.right)
            replace_node = new_tree.search_min()
            self.delete(replace_node.value)
            self.head.value = replace_node.value


        if direction == 'right':
            if not target_node.left and not target_node.right:
                parent_node.right = None
            elif not target_node.right:
                parent_node.right = target_node.left
            elif not target_node.left:
                parent_node.right = target_node.right
            else:
                new_tree = Tree(target_node.right)
                replace_node = new_tree.search_min()
            
                self.delete(replace_node.value)
                target_node.value = replace_node.value
                
        if direction == 'left':
            if not target_node.left and not target_node.right:
                parent_node.left = None
            elif not target_node.right:
                parent_node.left = target_node.left
            elif not target_node.left:
                parent_node.left = target_node.right
            else:
                new_tree = Tree(target_node.right)
                replace_node = new_tree.search_min()
                
                self.delete(replace_node.value)
                target_node.value = replace_node.value


    def search_min(self):
        if not self.head:
            return False
        tmp = self.head
        while tmp.left:
            tmp = tmp.left
        return tmp


    def tree_levels(self, level=0, levels = None):
        if levels is None:
            levels = {}

        if not self.head:
            return levels

        if not level in levels:
            levels[level] = []

        levels[level].append(self.head)
        if self.head.left:
            left_tree = Tree()
            left_tree.head = self.head.left
            left_tree.tree_levels(level+1, levels)

        if self.head.right:
            right_tree = Tree()
            right_tree.head = self.head.right
            right_tree.tree_levels(level+1, levels)

        return levels



    def conections_dict(self):
        levels = self.tree_levels()
        conections = {}
        conections_arr = []
        for key in levels:
            conections_arr = []
            for node in levels[key]:
                left_node, right_node = self.node_conections(node)
                if left_node and right_node:
                    conections_arr.append([node.value, left_node.value, right_node.value])
                elif left_node:
                    conections_arr.append([node.value, left_node.value])
                elif right_node:
                    conections_arr.append([node.value, right_node.value])
                else:
                    conections_arr.append([node.value])
            conections[key] = conections_arr
        return conections

    def node_conections(self, node):
        left_node = None
        right_node = None
        if not node.left and not node.right:
            return None, None
        if node.left:
            left_node = node.left.value
        if node.right:
            right_node = node.right.value
        return node.left, node.right

    def order_node_values(self):
        levels = self.tree_levels()
        node_values_ordered = []
        for key in levels:
            count = 0
            for node in levels[key]:
                node_values_ordered.append(node.value)
                count +=1
        return node_values_ordered

    def find_node_edges(self):
        # Edges (connections between nodes)
        edges = []
        node_conections_dict = self.conections_dict()
        print("Node conections:", node_conections_dict)
        for level in node_conections_dict:
            for conection_arr in node_conections_dict[level]:
                if len(conection_arr) == 2:
                    edges.append((conection_arr[0], conection_arr[1]))
                elif len(conection_arr) == 3:
                    edges.append((conection_arr[0], conection_arr[1]))
                    edges.append((conection_arr[0], conection_arr[2]))
        return edges

    def insert_middle(self, arr):
        if len(arr) == 1:
            self.insert(arr[0])
            return
        if len(arr) == 0:
            return
        self.insert(arr[int(len(arr)/2)])
        self.insert_middle(arr[:int(len(arr)/2)])
        self.insert_middle(arr[int(len(arr)/2)+1:])


    def balance_tree(self):
        ordered_nodes = sorted(self.order_node_values())
        balanced_tree = Tree()
        balanced_tree.insert_middle(ordered_nodes)
        return balanced_tree

    def tree_depth(self):
        levels = []
        tree_levels_dict = self.tree_levels()
        for key in tree_levels_dict:
            levels.append(key)
        return levels[-1]


    def is_balanced(self):
        node = self.head
        if not node.right and not node.left:
            return True
        elif node.left and node.right:
            left_tree = Tree()
            left_tree.head = node.left
            left_height = left_tree.tree_depth()

            right_tree = Tree()
            right_tree.head = node.right
            right_height = right_tree.tree_depth()

            if abs(left_height-right_height)<=1:
                left_balanced = left_tree.is_balanced()
                right_balanced = right_tree.is_balanced()
                if left_balanced and right_balanced:
                    return True
                else:
                    return False
        elif node.left:
            right_height = 0
            left_tree = Tree()
            left_tree.head = node.left
            left_height = left_tree.tree_depth()
            if abs(left_height-right_height)<=1:
                left_balanced = left_tree.is_balanced()
                if left_balanced:
                    return True
                else:
                    return False
        elif node.right:
            left_height = 0
            right_tree = Tree()
            right_tree.head = node.right
            right_height = right_tree.tree_depth()
            if abs(left_height-right_height)<=1:
                right_balanced = right_tree.is_balanced()
                if right_balanced:
                    return True
                else:
                    return False

        

