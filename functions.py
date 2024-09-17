from tree import *

def calculate_node_positions(node, x, y, x_offset, node_positions=None, level=0, order=None):
    if node_positions is None:
        node_positions = {}

    if order is None:
        order = []

    if not node:
        return node_positions, order

    # Assign position to the current node
    node_positions[node.value] = (x, y)
    order.append(node.value)

    # Reduce x_offset with depth
    if level >= 1:
        new_x_offset = x_offset / (1.5 * (level + 1))
    else:
        new_x_offset = x_offset / (1.6 * (level + 1))

    # Recur for the left and right subtrees
    if node.left:
        calculate_node_positions(node.left, x - new_x_offset, y + 150, x_offset, node_positions, level+1, order)
    
    if node.right:
        calculate_node_positions(node.right, x + new_x_offset, y + 150, x_offset, node_positions, level+1, order)

    return node_positions, order



def update_tree(btree, WIDTH=800, HEIGHT=600):
    print("___________________________________________________")
    node_values_ordered = btree.order_node_values()
    print("Node values ordered:", node_values_ordered)

    edges = btree.find_node_edges()
    print("Edges (conections)", edges)

    initial_x = WIDTH / 2 
    initial_y = 100  
    initial_x_offset = 200

    node_positions, order = calculate_node_positions(btree.head, initial_x, initial_y, initial_x_offset)
    scale = 1
    scale_arr = [1]
    for key in node_positions:
        node_x = node_positions[key][0]
        node_y = node_positions[key][1]
        if (HEIGHT/node_y < 1) or (WIDTH/node_x) < 1:
            if (WIDTH/node_x) > (HEIGHT/node_y):
                scale = HEIGHT/node_y - 0.06
            else:
                scale = WIDTH/node_x - 0.06
        scale_arr.append(scale)
    
    scale = sorted(scale_arr)[0]
        
    for key in node_positions:
        node_positions[key] = (node_positions[key][0]*scale, node_positions[key][1]*scale)

        #print(f"Node scale {key}: ", WIDTH/node_x, HEIGHT/node_y)

    print("Node positions:", node_positions)
    print("Node order for rendering:", order)

    return order, edges, node_positions, scale