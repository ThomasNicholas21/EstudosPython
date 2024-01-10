class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_non_recursive(root):
    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        count += 1

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return count

def count_nodes_recursive(root):
    if root is None:
        return 0

    return 1 + count_nodes_recursive(root.left) + count_nodes_recursive(root.right)

def sum_nodes_non_recursive(root):
    if root is None:
        return 0

    total_sum = 0
    stack = [root]

    while stack:
        node = stack.pop()
        total_sum += node.value

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return total_sum

def sum_nodes_recursive(root):
    if root is None:
        return 0

    return root.value + sum_nodes_recursive(root.left) + sum_nodes_recursive(root.right)

def tree_height_non_recursive(root):
    if root is None:
        return 0

    height = 0
    current_level = [root]

    while current_level:
        next_level = []

        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if next_level:
            height += 1
        current_level = next_level

    return height

def tree_height_recursive(root):
    if root is None:
        return 0

    left_height = tree_height_recursive(root.left)
    right_height = tree_height_recursive(root.right)

    return max(left_height, right_height) + 1

#exemplo de uso
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Número de nós (não recursivo):", count_nodes_non_recursive(root))
print("Número de nós (recursivo):", count_nodes_recursive(root))

print("Soma dos nós (não recursivo):", sum_nodes_non_recursive(root))
print("Soma dos nós (recursivo):", sum_nodes
