Tree Secondary Node Problem

A tree can be represented as a connected graph of g_nodes, numbered from 1 to g_nodes, where each edge connects two nodes. The i-th edge connects node g_from[i] to node g_to[i].

Suppose the maximum distance between any two nodes in the tree, denoted by mx, is the length of the longest path in the tree (diameter of the tree). A node is considered primary if it lies on the simple path between two nodes u and v such that the distance between u and v is equal to mx. All other nodes are considered secondary.

Note: The tree may have **multiple diameters**, i.e., more than one path of maximum length between different pairs of nodes.

Your task is to find the sum of the indices of all the secondary nodes.

Function Description
Complete the function getSecondaryNodeSum in the editor below.

getSecondaryNodeSum has the following parameters:
- int g_nodes: the number of nodes in the tree.
- int g_from[g_edges]: an array representing one end of each edge in the tree.
- int g_to[g_edges]: an array representing the other end of each edge in the tree.

Return:
- long int: the sum of the indices of the secondary nodes.

Constraints:
- 2 ≤ g_nodes ≤ 10^5
- 1 ≤ g_from[i], g_to[i] ≤ g_nodes
- g_edges = g_nodes - 1
- It is guaranteed that the edges form a tree.

Example

Input:
g_nodes = 6
g_edges = 5
g_from = [1, 1, 1, 2, 3]
g_to = [2, 3, 4, 5, 6]

Output:
4

Explanation:
The maximum distance between any two nodes is 4, for the pair (5, 6). The nodes on the path 5 --> 2 --> 1 --> 3 --> 6 are primary. The only secondary node is 4.

    1
   /|\
  2 3 4
  |   |
  5   6

Example 2

Input:
g_nodes = 5
g_edges = 4
g_from = [1, 1, 2, 2]
g_to = [2, 3, 4, 5]

Output:
0

Explanation:
The maximum distance between any two nodes is 3. All nodes lie on paths with maximum length, so there are no secondary nodes.

    1
   / \
  2   3
 / \
4   5
