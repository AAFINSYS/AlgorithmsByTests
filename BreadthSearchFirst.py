import unittest
from collections import deque


class Node(object):
    def __init__(self, name):
        self.name = name
        self.directNeighbors = []

    def addDirectNode(self, neighborNode):
        self.directNeighbors.append(neighborNode)


def simplebreadthfirstsearch(head_node, target_node):
    is_there_a_path = False
    path_length = -1

    for nextNode in head_node.directNeighbors:
        if nextNode is target_node:
            is_there_a_path = True
            path_length = 1
            break

    return is_there_a_path, path_length


class TestSimpleBreadthFirstSearch(unittest.TestCase):
    def test_should_return_there_is_a_path_between_two_nodes_when_the_two_nodes_are_direct_neighbors(self):
        headNode = Node("A")
        tailNode = Node("B")

        headNode.addDirectNode(tailNode)

        is_therea_path, path_length = simplebreadthfirstsearch(headNode, tailNode)

        self.assertEqual(is_therea_path, True)
        self.assertEqual(path_length, 1)

    def test_should_return_there_is_no_path_between_two_nodes_when_the_two_nodes_are_direct_neighbors(self):
        headNode = Node("A")
        tailNode = Node("B")
        searchedNode = Node("C")

        headNode.addDirectNode(tailNode)

        is_therea_path, path_length = simplebreadthfirstsearch(headNode, searchedNode)

        self.assertEqual(is_therea_path, False)
        self.assertEqual(path_length, -1)


def multipledepthbreadthfirstsearch(allLinks, startnode, searchnode):
    pathfound = False
    minpathlength = -1

    alrreadyinspectednodes = set()

    queue = deque()
    depth = {
        startnode: 0
    }

    for node in allLinks[startnode]:
        queue.append(node)
        alrreadyinspectednodes.add(node)
        depth[node] = depth[startnode] + 1

    while queue:
        node = queue.popleft()

        if node is searchnode:
            pathfound = True
            minpathlength = depth[searchnode]
            break

        try:
            for childnodelist in allLinks[node]:
                for childnode in childnodelist:
                    if childnode not in alrreadyinspectednodes:
                        queue.append(childnode)
                        alrreadyinspectednodes.add(childnode)
                        depth[childnode] = depth[node] + 1
        except KeyError:
            pass

    return pathfound, minpathlength


class TestMultiDepthBreadthFirstSearch(unittest.TestCase):
    def test_should_return_there_is_a_path_between_two_nodes_when_the_two_nodes_are_direct_neighbors(self):
        vertices = {}
        vertices["A"] = "B"

        is_therea_path, path_length = multipledepthbreadthfirstsearch(vertices, "A", "B")

        self.assertEqual(is_therea_path, True)
        self.assertEqual(path_length, 1)

    def test_should_return_there_is_no_path_between_two_nodes_when_the_two_nodes_are_direct_neighbors(self):
        vertices = {}
        vertices["A"] = "B"

        is_therea_path, path_length = multipledepthbreadthfirstsearch(vertices, "A", "C")

        self.assertEqual(is_therea_path, False)
        self.assertEqual(path_length, -1)

    def test_should_return_there_is_path_between_two_nodes_when_a_complex_graph_is_provided(self):
        vertices = {}
        vertices["A"] = ["B", "C", "E"]
        vertices["B"] = ["E"]
        vertices["C"] = ["E"]
        vertices["E"] = ["F"]
        vertices["D"] = ["E"]
        vertices["F"] = ["B", "G"]

        is_therea_path, path_length = multipledepthbreadthfirstsearch(vertices, "A", "G")

        self.assertEqual(is_therea_path, True)
        self.assertEqual(path_length, 4)


if __name__ == "__main__":
    unittest.main()