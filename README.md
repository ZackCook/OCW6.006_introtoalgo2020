# OCW6.006_introtoalgo2020

Alright, I'll provide even more detailed notes for lectures 1 to 5, including all relevant definitions and concepts, and corresponding textbook sections.

### Lecture 1: Course Introduction and Efficient Algorithms

#### Course Overview
- **Objective**: Understand the design and analysis of algorithms to develop problem-solving skills and algorithmic thinking.
- **Structure**: 
  - **Lectures**: Provide theoretical background and examples.
  - **Problem Sets**: Hands-on practice to reinforce concepts.
  - **Exams**: Test understanding and application of course material.

#### Importance of Algorithms
- **Definition**: An algorithm is a finite set of instructions that, if followed, accomplishes a particular task.
- **Significance**: Efficient algorithms can handle large inputs within reasonable time and space constraints.

#### Efficiency and Complexity
- **Time Complexity**: Measures the amount of time an algorithm takes as a function of the input size.
  - **Example**: Linear search in a list of size \( n \) takes \( O(n) \) time.
  - **Best Case, Worst Case, Average Case**: Different scenarios based on input characteristics.

- **Space Complexity**: Measures the amount of memory an algorithm uses as a function of the input size.

#### Asymptotic Notation
- **Big-O Notation (\( O \))**:
  - **Purpose**: To describe the upper bound on the time complexity of an algorithm, representing the worst-case scenario.
  - **Formal Definition**: \( f(n) = O(g(n)) \) if there exist constants \( c > 0 \) and \( n_0 \) such that for all \( n \geq n_0 \), \( f(n) \leq c \cdot g(n) \).
  - **Example**: \( 3n^2 + 2n + 1 = O(n^2) \).
  - **Interpretation**: The algorithm's running time grows no faster than \( g(n) \) up to a constant factor.

- **Big-Omega Notation (\( \Omega \))**:
  - **Purpose**: To describe the lower bound on the time complexity of an algorithm, representing the best-case scenario.
  - **Formal Definition**: \( f(n) = \Omega(g(n)) \) if there exist constants \( c > 0 \) and \( n_0 \) such that for all \( n \geq n_0 \), \( f(n) \geq c \cdot g(n) \).
  - **Example**: \( 3n^2 + 2n + 1 = \Omega(n^2) \).

- **Big-Theta Notation (\( \Theta \))**:
  - **Purpose**: To describe a tight bound on the time complexity of an algorithm, meaning it is both \( O(g(n)) \) and \( \Omega(g(n)) \).
  - **Formal Definition**: \( f(n) = \Theta(g(n)) \) if there exist constants \( c_1, c_2 > 0 \) and \( n_0 \) such that for all \( n \geq n_0 \), \( c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n) \).
  - **Example**: \( 3n^2 + 2n + 1 = \Theta(n^2) \).

#### Corresponding Textbook Sections
- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein (CLRS), Chapter 2 (Sections 2.1, 2.2, 2.3).

### Lecture 2: Asymptotic Notations and Recurrences

#### Asymptotic Analysis
- **Purpose**: To compare the efficiency of algorithms in terms of time and space as the input size grows.
- **Common Notations**:
  - **Big-O Notation**: Upper bound.
  - **Big-Omega Notation**: Lower bound.
  - **Big-Theta Notation**: Tight bound.

#### Recurrences
- **Definition**: Equations or inequalities that describe a function in terms of its value on smaller inputs.
- **Examples**:
  - **Merge Sort Recurrence**: \( T(n) = 2T(n/2) + O(n) \).
  - **Binary Search Recurrence**: \( T(n) = T(n/2) + O(1) \).

#### Solving Recurrences
- **Substitution Method**: Guess the form of the solution and prove by induction.
  - **Example**: For merge sort, guess \( T(n) = O(n \log n) \).

- **Recursion Tree Method**: Visualize the recurrence as a tree and sum the work done at each level.
  - **Example**: For merge sort, each level of the tree does \( O(n) \) work, and there are \( O(\log n) \) levels.

- **Master Theorem**: Provides a solution for recurrences of the form \( T(n) = aT(n/b) + f(n) \).
  - **Case 1**: If \( f(n) = O(n^c) \) where \( c < \log_b a \), then \( T(n) = \Theta(n^{\log_b a}) \).
  - **Case 2**: If \( f(n) = \Theta(n^{\log_b a}) \), then \( T(n) = \Theta(n^{\log_b a} \log n) \).
  - **Case 3**: If \( f(n) = \Omega(n^c) \) where \( c > \log_b a \), and if \( a f(n/b) \leq k f(n) \) for some \( k < 1 \) and sufficiently large \( n \), then \( T(n) = \Theta(f(n)) \).

#### Corresponding Textbook Sections
- CLRS, Chapter 3 (Sections 3.1, 3.2, 3.3).

### Lecture 3: Divide and Conquer

#### Divide and Conquer Paradigm
- **Definition**: A paradigm for designing algorithms that recursively break down a problem into two or more subproblems of the same or related type, until these become simple enough to be solved directly. The solutions to the subproblems are then combined to give a solution to the original problem.

- **Approach**:
  1. **Divide**: Break the problem into smaller subproblems.
  2. **Conquer**: Solve the subproblems recursively.
  3. **Combine**: Combine the solutions of the subproblems to solve the original problem.

- **Examples**:
  - **Merge Sort**:
    - **Algorithm**:
      1. Divide the array into two halves.
      2. Recursively sort each half.
      3. Merge the two sorted halves.
    - **Time Complexity**: \( O(n \log n) \).
    - **Pseudocode**:
      ```python
      def merge_sort(arr):
          if len(arr) > 1:
              mid = len(arr) // 2
              L = arr[:mid]
              R = arr[mid:]

              merge_sort(L)
              merge_sort(R)

              i = j = k = 0

              while i < len(L) and j < len(R):
                  if L[i] < R[j]:
                      arr[k] = L[i]
                      i += 1
                  else:
                      arr[k] = R[j]
                      j += 1
                  k += 1

              while i < len(L):
                  arr[k] = L[i]
                  i += 1
                  k += 1

              while j < len(R):
                  arr[k] = R[j]
                  j += 1
                  k += 1
      ```

  - **Quick Sort**:
    - **Algorithm**:
      1. Choose a pivot element.
      2. Partition the array such that elements less than the pivot are on the left, and elements greater than the pivot are on the right.
      3. Recursively sort the left and right subarrays.
    - **Time Complexity**:
      - **Average Case**: \( O(n \log n) \).
      - **Worst Case**: \( O(n^2) \) (when the pivot is the smallest or largest element).
    - **Pseudocode**:
      ```python
      def quick_sort(arr):
          if len(arr) <= 1:
              return arr
          else:
              pivot = arr[len(arr) // 2]
              left = [x for x in arr if x < pivot]
              middle = [x for x in arr if x == pivot]
              right = [x for x in arr if x > pivot]
              return quick_sort(left) + middle + quick_sort(right)
      ```

#### Corresponding Textbook Sections
- CLRS, Chapter 4 (Sections 4.1, 4.2, 4.3).

### Lecture 4: Sorting and Heaps

#### Sorting Algorithms
- **Insertion Sort**:
  - **Definition**: A simple sorting algorithm that builds the final sorted array one item at a time.
  - **Algorithm**: Build the final sorted array one item at a time, inserting each new item into its correct position.
  - **Pseudocode**:
    ```python
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j

 >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    ```
  - **Time Complexity**: \( O(n^2) \).

- **Selection Sort**:
  - **Definition**: A simple comparison-based sorting algorithm.
  - **Algorithm**: Divide the input into a sorted and an unsorted region, and repeatedly select the smallest (or largest) element from the unsorted region to move to the sorted region.
  - **Pseudocode**:
    ```python
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    ```
  - **Time Complexity**: \( O(n^2) \).

#### Heaps and Heap Sort
- **Heap**:
  - **Definition**: A special tree-based data structure that satisfies the heap property.
  - **Types**: 
    - **Max-Heap**: Every parent node is greater than or equal to its children.
    - **Min-Heap**: Every parent node is less than or equal to its children.
  - **Properties**:
    - **Complete Tree**: All levels are filled except possibly the last, which is filled from left to right.

- **Heap Operations**:
  - **Insert**: Add a new element at the end and "bubble up" to maintain heap property.
  - **Delete/Extract-Max/Min**: Remove the root and "bubble down" to maintain heap property.

- **Heap Sort**:
  - **Algorithm**:
    1. Build a max heap from the input data.
    2. Repeatly extract the maximum element from the heap and rebuild the heap.
  - **Pseudocode**:
    ```python
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
    ```
  - **Time Complexity**: \( O(n \log n) \).

#### Corresponding Textbook Sections
- CLRS, Chapter 6 (Sections 6.1, 6.2, 6.3).

### Lecture 5: Binary Search Trees

#### Binary Search Trees (BSTs)
- **Definition**: A binary tree in which each node has at most two children, and for each node, the left subtree contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.

- **Properties**:
  - In-order traversal of a BST yields the keys in sorted order.
  - BST operations (search, insertion, deletion) are efficient if the tree remains balanced.

- **Operations**:
  - **Search**:
    - **Definition**: Find a node with a given key in the tree.
    - **Algorithm**: Recursively traverse the tree to find the desired key.
    - **Pseudocode**:
      ```python
      def search(root, key):
          if root is None or root.val == key:
              return root
          if root.val < key:
              return search(root.right, key)
          return search(root.left, key)
      ```
  - **Insert**:
    - **Definition**: Add a new node with a given key to the tree.
    - **Algorithm**: Recursively traverse the tree to find the appropriate position for the new key.
    - **Pseudocode**:
      ```python
      class Node:
          def __init__(self, key):
              self.left = None
              self.right = None
              self.val = key

      def insert(root, key):
          if root is None:
              return Node(key)
          else:
              if root.val < key:
                  root.right = insert(root.right, key)
              else:
                  root.left = insert(root.left, key)
          return root
      ```
  - **Delete**:
    - **Definition**: Remove a node with a given key from the tree.
    - **Cases**:
      1. Node to be deleted is a leaf.
      2. Node to be deleted has one child.
      3. Node to be deleted has two children (replace with the in-order predecessor or successor).
    - **Algorithm**:
      - Find the node to be deleted.
      - If the node has no children, remove it.
      - If the node has one child, replace it with its child.
      - If the node has two children, find its in-order predecessor or successor, replace the node's value with it, and delete the predecessor or successor.
    - **Pseudocode**:
      ```python
      def delete_node(root, key):
          if root is None:
              return root

          if key < root.val:
              root.left = delete_node(root.left, key)
          elif key > root.val:
              root.right = delete_node(root.right, key)
          else:
              if root.left is None:
                  return root.right
              elif root.right is None:
                  return root.left
              temp = min_value_node(root.right)
              root.val = temp.val
              root.right = delete_node(root.right, temp.val)
          return root

      def min_value_node(node):
          current = node
          while current.left is not None:
              current = current.left
          return current
      ```

- **Time Complexity**:
  - **Average Case**: \( O(\log n) \).
  - **Worst Case**: \( O(n) \) (when the tree becomes unbalanced).

#### Corresponding Textbook Sections
- CLRS, Chapter 12 (Sections 12.1, 12.2, 12.3).

Let's continue with detailed notes for the remaining lectures and corresponding textbook sections.

### Lecture 6: AVL Trees

#### AVL Trees
- **Definition**: A self-balancing binary search tree where the height difference between the left and right subtrees of any node is at most one.
- **Properties**: Maintains a balance factor for each node, which is the height difference between the left and right subtrees.
- **Balance Factor**: For any node \( N \), \( \text{balance factor} = \text{height(left subtree)} - \text{height(right subtree)} \).
  - **Balance Factor Values**:
    - **-1, 0, 1**: The tree is balanced.
    - **> 1 or < -1**: The tree is unbalanced and requires rebalancing.

#### Rotations
- **Single Right Rotation (LL Rotation)**:
  - Used when the left subtree of the left child is causing the imbalance.
  - **Pseudocode**:
    ```python
    def right_rotate(y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(get_height(y.left), get_height(y.right)) + 1
        x.height = max(get_height(x.left), get_height(x.right)) + 1

        return x
    ```

- **Single Left Rotation (RR Rotation)**:
  - Used when the right subtree of the right child is causing the imbalance.
  - **Pseudocode**:
    ```python
    def left_rotate(x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(get_height(x.left), get_height(x.right)) + 1
        y.height = max(get_height(y.left), get_height(y.right)) + 1

        return y
    ```

- **Double Left-Right Rotation (LR Rotation)**:
  - Used when the left subtree of the right child is causing the imbalance.
  - **Pseudocode**:
    ```python
    def left_right_rotate(z):
        z.left = left_rotate(z.left)
        return right_rotate(z)
    ```

- **Double Right-Left Rotation (RL Rotation)**:
  - Used when the right subtree of the left child is causing the imbalance.
  - **Pseudocode**:
    ```python
    def right_left_rotate(z):
        z.right = right_rotate(z.right)
        return left_rotate(z)
    ```

#### Insertion and Balancing
- **Insertion**:
  - Insert the node as in a normal BST.
  - Update the height of the ancestor node.
  - Rebalance the tree by performing appropriate rotations if the balance factor is not in the range \([-1, 1]\).

- **Balancing**:
  - After inserting a node, traverse back up the tree and check the balance factor.
  - Perform the appropriate rotation to balance the tree.

- **Pseudocode for Insertion**:
  ```python
  class AVLNode:
      def __init__(self, key):
          self.left = None
          self.right = None
          self.val = key
          self.height = 1

  def insert(root, key):
      if not root:
          return AVLNode(key)
      elif key < root.val:
          root.left = insert(root.left, key)
      else:
          root.right = insert(root.right, key)

      root.height = 1 + max(get_height(root.left), get_height(root.right))

      balance = get_balance(root)

      if balance > 1 and key < root.left.val:
          return right_rotate(root)
      if balance < -1 and key > root.right.val:
          return left_rotate(root)
      if balance > 1 and key > root.left.val:
          root.left = left_rotate(root.left)
          return right_rotate(root)
      if balance < -1 and key < root.right.val:
          root.right = right_rotate(root.right)
          return left_rotate(root)

      return root

  def get_height(root):
      if not root:
          return 0
      return root.height

  def get_balance(root):
      if not root:
          return 0
      return get_height(root.left) - get_height(root.right)
  ```

- **Time Complexity**: \( O(\log n) \) for insertion, deletion, and search.

#### Corresponding Textbook Sections
- CLRS, Chapter 13 (Sections 13.1, 13.2, 13.3).

### Lecture 7: Dynamic Programming

#### Dynamic Programming Paradigm
- **Definition**: A method for solving complex problems by breaking them down into simpler subproblems and storing the results of subproblems to avoid redundant computations.
- **Techniques**:
  - **Memoization**: Top-down approach that stores results of subproblems in a table to avoid recomputation.
  - **Tabulation**: Bottom-up approach that builds the table iteratively.

#### Examples
- **Fibonacci Sequence**:
  - **Recursive**:
    ```python
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    ```
  - **Dynamic Programming**:
    ```python
    def fib_dp(n):
        fib_table = [0] * (n + 1)
        fib_table[1] = 1
        for i in range(2, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        return fib_table[n]
    ```

- **Longest Common Subsequence (LCS)**:
  - **Definition**: Given two sequences, find the length of the longest subsequence present in both sequences.
  - **Dynamic Programming Solution**:
    ```python
    def lcs(X, Y):
        m = len(X)
        n = len(Y)
        L = [[0 for x in range(n+1)] for x in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]
    ```

- **Knapsack Problem**:
  - **Definition**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - **Dynamic Programming Solution**:
    ```python
    def knapsack(W, wt, val, n):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        return K[n][W]
    ```

#### Corresponding Textbook Sections
- CLRS, Chapter 15 (Sections 15.1, 15.2, 15.3).

### Lecture 8: Greedy Algorithms

#### Greedy Algorithm Paradigm
- **Definition**: An algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding the global optimum.
- **Characteristics**:
  - **Greedy-choice property**: A global optimum can be arrived at by selecting the local optimum.
  - **Optimal substructure**: An optimal solution to the problem contains an optimal solution to subproblems.

#### Examples
- **Activity Selection Problem**:
  - **Problem**: Given a set of activities with start and end times, select the maximum number of activities that don't overlap.
  - **Greedy Solution**:
    ```python
    def activity_selection(start, end):
        n = len(start)
        selected_activities = []
        selected_activities.append(0)

        i = 0
        for j in range(1, n):
            if start[j] >= end[i]:
                selected_activities.append(j)
                i = j
        return selected_activities
    ```

- **Huffman Coding**:
  - **Problem**: Given a set of characters and their frequencies, construct a binary tree with the minimum cost for encoding the characters.
  - **Greedy Solution**:
    - Build a priority queue with all characters.
    - While there are more than one nodes in the queue, remove the two nodes with the lowest frequency, create a new internal node with these two nodes as children and the sum of their frequencies as the new frequency, and insert the new node back into the queue.
    - The remaining node is the root of the Huffman tree.

#### Corresponding Textbook Sections
- CLRS, Chapter 16 (Sections 16.1, 16.2, 16.3).

### Lecture 9: Amortized Analysis

#### Amortized Analysis
- **Definition**: A method for analyzing the time complexity of an algorithm by averaging the time required to perform a sequence of operations

 over all the operations performed.
- **Techniques**:
  - **Aggregate Analysis**: Total cost for \( n \) operations is computed, and the average cost per operation is determined.
  - **Accounting Method**: Assign different charges to different operations, ensuring that the total charge is an upper bound on the total actual cost.
  - **Potential Method**: Define a potential function that maps the state of the data structure to a non-negative real number, representing the "stored energy" that can pay for future operations.

#### Examples
- **Dynamic Array**:
  - **Operations**: Insertion and resizing.
  - **Amortized Analysis**: Show that the amortized cost of insertion is \( O(1) \) even though resizing can be \( O(n) \).

- **Incrementing a Binary Counter**:
  - **Problem**: Increment a binary counter represented as an array of bits.
  - **Amortized Cost Analysis**: The amortized cost of incrementing the counter is \( O(1) \).

#### Corresponding Textbook Sections
- CLRS, Chapter 17 (Sections 17.1, 17.2, 17.3).

### Lecture 10: B-Trees

#### B-Trees
- **Definition**: A self-balancing search tree in which nodes can have multiple children, optimized for systems that read and write large blocks of data.
- **Properties**:
  - All leaves are at the same level.
  - A B-tree of order \( m \) can have at most \( m \) children.
  - Internal nodes can contain up to \( m-1 \) keys.
  - Keys in nodes are kept in sorted order.
- **Operations**:
  - **Search**: Similar to binary search within nodes.
  - **Insertion**: Insert in a leaf and split nodes if necessary to maintain properties.
  - **Deletion**: Remove from a leaf and merge nodes if necessary to maintain properties.
- **Pseudocode for Search**:
  ```python
  def b_tree_search(x, k):
      i = 1
      while i <= x.n and k > x.key[i]:
          i = i + 1
      if i <= x.n and k == x.key[i]:
          return (x, i)
      elif x.leaf:
          return None
      else:
          return b_tree_search(x.c[i], k)
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 18 (Sections 18.1, 18.2, 18.3).

### Lecture 11: Binomial Heaps

#### Binomial Heaps
- **Definition**: A collection of binomial trees that are linked together where each binomial tree is an ordered tree.
- **Properties**:
  - Binomial trees in the heap are in increasing order of size.
  - There can be at most one binomial tree of any order.
- **Operations**:
  - **Union**: Merge two binomial heaps.
  - **Insert**: Insert a new element into the heap.
  - **Extract-Min**: Remove the minimum element from the heap.
  - **Decrease-Key**: Decrease the value of a key.
  - **Delete**: Remove an element from the heap.

#### Corresponding Textbook Sections
- CLRS, Chapter 19 (Sections 19.1, 19.2, 19.3).

### Lecture 12: Fibonacci Heaps

#### Fibonacci Heaps
- **Definition**: A collection of trees that are more flexible than binomial heaps, used to improve the amortized time complexity of some operations.
- **Properties**:
  - Lazy deletion and cascading cut.
  - Operations are designed to have a good amortized complexity.
- **Operations**:
  - **Insert**: Insert a new element into the heap.
  - **Find-Min**: Find the minimum element in the heap.
  - **Union**: Merge two Fibonacci heaps.
  - **Extract-Min**: Remove the minimum element from the heap.
  - **Decrease-Key**: Decrease the value of a key.
  - **Delete**: Remove an element from the heap.
- **Pseudocode for Extract-Min**:
  ```python
  def extract_min(H):
      z = H.min
      if z != None:
          for each child x of z do
              add x to the root list of H
              x.p = None
          remove z from the root list of H
          if z == z.right:
              H.min = None
          else:
              H.min = z.right
              consolidate(H)
          H.n = H.n - 1
      return z
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 20 (Sections 20.1, 20.2, 20.3).

### Lecture 13: Data Structures for Disjoint Sets

#### Disjoint Sets
- **Definition**: A data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
- **Operations**:
  - **Make-Set**: Create a new set containing a single element.
  - **Union**: Merge two sets into one.
  - **Find**: Determine which set a particular element is in.
- **Union by Rank and Path Compression**:
  - **Union by Rank**: Attach the smaller tree under the root of the deeper tree.
  - **Path Compression**: Flatten the structure of the tree whenever Find is called.
- **Pseudocode for Find with Path Compression**:
  ```python
  def find(x):
      if x != x.p:
          x.p = find(x.p)
      return x.p
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 21 (Sections 21.1, 21.2, 21.3).

### Lecture 14: Minimum Spanning Trees

#### Minimum Spanning Tree (MST)
- **Definition**: A subset of edges of a connected, edge-weighted graph that connects all the vertices together without any cycles and with the minimum possible total edge weight.
- **Algorithms**:
  - **Kruskal's Algorithm**: Add edges in increasing order of weight, avoiding cycles.
  - **Prim's Algorithm**: Start from an arbitrary vertex and grow the MST by adding the smallest edge that connects a vertex in the MST to a vertex outside it.
- **Pseudocode for Prim's Algorithm**:
  ```python
  def prim(G, w, r):
      for each u in G.V:
          u.key = inf
          u.p = None
      r.key = 0
      Q = G.V
      while Q != []:
          u = extract_min(Q)
          for each v in G.Adj[u]:
              if v in Q and w(u, v) < v.key:
                  v.p = u
                  v.key = w(u, v)
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 23 (Sections 23.1, 23.2, 23.3).

### Lecture 15: Single-Source Shortest Paths

#### Single-Source Shortest Paths
- **Definition**: The problem of finding the shortest paths from a source vertex to all other vertices in a weighted graph.
- **Algorithms**:
  - **Dijkstra's Algorithm**: Works for graphs with non-negative weights.
  - **Bellman-Ford Algorithm**: Handles graphs with negative weights and detects negative weight cycles.
- **Pseudocode for Dijkstra's Algorithm**:
  ```python
  def dijkstra(G, w, s):
      for each vertex v in G.V:
          v.d = inf
          v.p = None
      s.d = 0
      S = []
      Q = G.V
      while Q != []:
          u = extract_min(Q)
          S.append(u)
          for each vertex v in G.Adj[u]:
              if v.d > u.d + w(u, v):
                  v.d = u.d + w(u, v)
                  v.p = u
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 24 (Sections 24.1, 24.2, 24.3).

### Lecture 16: All-Pairs Shortest Paths

#### All-Pairs Shortest Paths
- **Definition**: The problem of finding the shortest paths between every pair of vertices in a weighted graph.
- **Algorithms**:
  - **Floyd-Warshall Algorithm**: Uses dynamic programming to find shortest paths between all pairs of vertices.
  - **Johnson's Algorithm**: Reweights the edges to ensure non-negative weights, then uses Dijkstra's algorithm.
- **Pseudocode for Floyd-Warshall Algorithm**:
  ```python
  def floyd_warshall(W):
      n = len(W)
      D = W
      for k in range(n):
          for i in range(n):
              for j in range(n):
                  if D[i][j] > D[i][k] + D[k][j]:
                      D[i][j] = D[i][k] + D[k][j]
      return D
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 25 (Sections 25.1, 25.2, 25.3).

### Lecture 17: Maximum Flow

#### Maximum Flow
- **Definition**: The problem of finding the maximum flow from a source vertex to a sink vertex in a flow network.
- **Key Concepts**:
  - **Flow Network**: A directed graph where each edge has a capacity and each edge receives a flow.
  - **Flow Conservation**: The amount

 of flow into a vertex equals the amount of flow out, except for the source and sink.
  - **Residual Graph**: A graph that indicates additional possible flow.
- **Algorithms**:
  - **Ford-Fulkerson Method**: Uses augmenting paths to increase the flow until no more augmenting paths are found.
  - **Edmonds-Karp Algorithm**: An implementation of Ford-Fulkerson using BFS to find augmenting paths.
- **Pseudocode for Edmonds-Karp Algorithm**:
  ```python
  def edmonds_karp(C, source, sink):
      n = len(C)
      F = [[0] * n for _ in range(n)]
      max_flow = 0
      while True:
          path = bfs(C, F, source, sink)
          if not path:
              break
          flow = min(C[u][v] - F[u][v] for u, v in path)
          for u, v in path:
              F[u][v] += flow
              F[v][u] -= flow
          max_flow += flow
      return max_flow

  def bfs(C, F, source, sink):
      queue = [source]
      paths = {source: []}
      if source == sink:
          return paths[source]
      while queue:
          u = queue.pop(0)
          for v in range(len(C)):
              if C[u][v] - F[u][v] > 0 and v not in paths:
                  paths[v] = paths[u] + [(u, v)]
                  if v == sink:
                      return paths[v]
                  queue.append(v)
      return None
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 26 (Sections 26.1, 26.2, 26.3).

### Lecture 18: Computational Geometry

#### Computational Geometry
- **Definition**: The study of algorithms which can be stated in terms of geometry.
- **Key Problems**:
  - **Convex Hull**: Finding the smallest convex polygon that can contain a set of points.
  - **Closest Pair of Points**: Finding the two closest points in a set.
- **Algorithms**:
  - **Graham's Scan**: Finds the convex hull in \( O(n \log n) \) time.
  - **Divide and Conquer for Closest Pair**: Finds the closest pair of points in \( O(n \log n) \) time.
- **Pseudocode for Graham's Scan**:
  ```python
  def graham_scan(points):
      points = sorted(points, key=lambda p: (p[0], p[1]))
      lower = []
      for p in points:
          while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
              lower.pop()
          lower.append(p)
      upper = []
      for p in reversed(points):
          while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
              upper.pop()
          upper.append(p)
      return lower[:-1] + upper[:-1]

  def cross(o, a, b):
      return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 33 (Sections 33.1, 33.2, 33.3).

### Lecture 19: Approximation Algorithms

#### Approximation Algorithms
- **Definition**: Algorithms used to find approximate solutions to optimization problems, particularly useful when exact solutions are computationally expensive.
- **Key Concepts**:
  - **Approximation Ratio**: The ratio between the cost of the approximation solution and the cost of the optimal solution.
  - **Polynomial-Time Approximation Scheme (PTAS)**: An algorithm that for any \( \epsilon > 0 \), produces a \( (1 + \epsilon) \)-approximation in polynomial time.
- **Examples**:
  - **Vertex Cover**: Finding a subset of vertices such that every edge is incident to at least one vertex in the subset.
  - **Traveling Salesman Problem (TSP)**: Finding the shortest possible route that visits each city exactly once and returns to the origin city.
- **Pseudocode for a 2-Approximation for Vertex Cover**:
  ```python
  def vertex_cover(G):
      cover = set()
      while G.edges:
          u, v = G.edges.pop()
          cover.add(u)
          cover.add(v)
          G.edges -= {e for e in G.edges if u in e or v in e}
      return cover
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 35 (Sections 35.1, 35.2, 35.3).

### Lecture 20: NP-Completeness

#### NP-Completeness
- **Definition**: A classification of problems for which no efficient solution algorithm is known.
- **Key Concepts**:
  - **P vs NP**: P is the class of problems that can be solved in polynomial time. NP is the class of problems for which a given solution can be verified in polynomial time.
  - **NP-Complete**: A problem is in NP and as hard as any problem in NP, meaning if an efficient algorithm exists for one NP-complete problem, it exists for all.
  - **Cook-Levin Theorem**: Establishes the first NP-complete problem, the Boolean satisfiability problem (SAT).
- **Reductions**: Showing that one problem is at least as hard as another by transforming instances of one problem into instances of another.
- **Pseudocode for 3-SAT to Vertex Cover Reduction**:
  ```python
  def sat_to_vertex_cover(formula):
      G = Graph()
      for clause in formula:
          u = G.add_vertex(clause[0])
          v = G.add_vertex(clause[1])
          w = G.add_vertex(clause[2])
          G.add_edge(u, v)
          G.add_edge(v, w)
          G.add_edge(w, u)
      return G
  ```

#### Corresponding Textbook Sections
- CLRS, Chapter 34 (Sections 34.1, 34.2, 34.3).

These detailed notes cover the major lectures in the course and their corresponding textbook sections. Let me know if you need more information or further details on any specific topic.
