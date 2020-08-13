## Trees with WWCode SV
### What?
A tree is a data structure for storage with nodes and edges. A hierarchical data structure with one root node, at top. Root branches down and nodes grow downward. Multiple levels of children.
If sorted, smaller values on left side, larger values on right.
Usually we are given access to the root, and reach other nodes through traversal. However, you can have a table storing pointers which give direct access to children.
Usually unidirectional from parent to child.
A node can have any number of children.

### Why?
Used in interviews to check understanding of recursion, queues, time complexity. Correct answers are often clean and compact.
Used to implement simple sorting algorithms
Used in many search applications where data are constantly entering/leaving
Used in real world applications: expression parsers, caches, garbage collectors.

### Features
Node: Element that contains a value and pointers to children.
Root: Node at the top. Entry point. Top most parent. Only one path from root to any note.
Path: Sequence of edges to get from one node to another
Parent: The node upstream to another node.
Child: Node(s) Downstream to another node. # can vary
Levels/Layers: Represent generations of children nodes from the previous parent and roots.
Leaf: Nodes at the bottom most level, with no children.
Subtree: All subsequent descendants of a node.
Depth: Number of steps from the root to N. Root has depth 0.
Height: Greatest depth of any node in the tree. Tells us the time complexity of the tree.
Traversing: Passing through nodes in a certain order.
Visiting: Checking the value of a node.
Balanced: Number of nodes on left and right are same. For a reasonably balanced tree, traversal is in O(log(n)) of the height.

### Common Types
Binary: Nodes have max 2 children.
BST: Binary Tree meeting specific properties. Very useful for searching. Left<= Node <= Right.
AVL Trees: Self-balancing BST. Each nodes stores a value called a balance factor which is the difference in height between its left subtree and right subtree.
Red-Black Tree: Another self-balancing BST. Each node is marked as red or black.
N-ary tree: Tree with N children. Special N-ary Tree - Trie. Children nodes are based on characters of the alphabet, each leaf child makes an actual word.

### Tree Traversals
Depth First Search (DFS):
- Start at root, explore path going to the deepest levels (leaves) first
- Backtrack upwards to explore path leading to another leaf node
- Logarithmic advantage, as reducing the scope of elements need to look at
- Oftentimes uses recursion

Breath First Search (BFS):
- Start at root, explore closest neighboring levels first
- After each level, proceed to a level father away from root
- If doing a lot of BFS, tree may be the wrong structure as you're not taking advantage of the logarithmic reduction
- Oftentimes uses a queue

#### Three Common DFS
Pre-order: 1-2-3-4-5-6-7
- Check current node's value
- Visit left node
- Visit right node

In-order: 3-2-4-1-6-5-7
- Left
- Current
- Right

Post-order: 3-4-2-6-7-5-1
- Left
- Right
- Current

BFS: Go through until your queue is empty, enqueueing the child nodes. Can to L to R, R to L or even zig zag.

Time Complexity:

| Operation | Binary Tree | BST |
| ----------- | ----------- | ----------- |
Search | O(n) Worst case goes through every element | O(h) where h is height. <br>Decently balanced tree h=log(n)<br> worst case h = n.
Insert| O(1) if insert is at root. <br>O(h): h= log(n) if insert at deepest level of balanced tree h=n if unbalanced | O(h) where h is as above
Remove| O(n) worst case, go through every element | O(h) where h as above

When interviewing, draw out the tree.
Find a good tree example
-Not too Balanced
- Include special/corner cases
- Tree with
  - mix of 0,1,2 Children
  - single Leaf
  - more children on one side than the other
