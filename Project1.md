* Sorting visualizer *

Part 1
- Implement a sorting analyzer for bubble, insertion, selection and merge (Python)
- sorting visualizer will be updated with other sorting algorithms as course progresses

Part 2
- Hand roll a dynamic array, linked-list, stack and hash table with all operations implmented (Scala)
- write driver programs for each DS that allows a user to unsert and delete data as well as perform any unique operations

DynamicArray Class
Class Declaration:
  Define a class named DynamicArray that takes an initial capacity as a parameter.
Private Variables:
  Declare a private array to store integers.
  Declare a private variable to keep track of the current size of the dynamic array.
Methods 
  Size Method: Implement a method that returns the current size of the dynamic array.
  IsEmpty Method: Implement a method that returns a Boolean indicating whether the dynamic array is empty.
  Add Method: Implement a method to add an integer to the dynamic array. Ensure this method resizes the array if it is full.
  Get Method: Implement a method to retrieve an integer at a specified index. Ensure this method checks if the index is within bounds and throws an appropriate exception if not.
  Resize Method: Implement a private method that doubles the capacity of the array when it is full. This method should create a new array with twice the capacity, copy existing elements to the new array, and update the reference to the new array.

- Linked List
Class Declaration
  Define a class named LinkedList.
Node Class
  Define a private inner class Node with the following properties:
  Data: stores the value of the node.
  Next: stores a reference to the next node in the list.
Private Variables
  Head: a reference to the first node in the list.
  Size: an integer to keep track of the number of elements in the list.
Methods
  Size Method: Return the current size of the linked list.
  IsEmpty Method: Return a Boolean indicating whether the linked list is empty.
  Add Method: Add a new element to the end of the list.
  AddAt Method: Add a new element at a specified index.
  Remove Method: Remove an element from the list.
  RemoveAt Method: Remove an element at a specified index.
  Get Method: Retrieve an element at a specified index.
  
Stack
Class Declaration
  Define a class named Stack.
Private Variables
  An array or list to store the stack elements.
  Size: an integer to keep track of the number of elements in the stack.
Methods
  Size Method: Return the current size of the stack.
  IsEmpty Method: Return a Boolean indicating whether the stack is empty.
  Push Method: Add a new element to the top of the stack.
  Pop Method: Remove and return the top element of the stack.
  Peek Method: Return the top element without removing it.
  
Hash Table
Class Declaration
  Define a class named HashTable.
Node Class
  Define a private inner class Node with the following properties:
  Key: stores the key of the entry.
  Value: stores the value of the entry.
  Next: stores a reference to the next node in case of collisions (chaining).
Private Variables
  Table: an array to store the entries (buckets).
  Size: an integer to keep track of the number of elements in the table.
  Capacity: an integer to define the initial capacity of the table.
Methods
  Size Method: Return the current size of the hash table.
  IsEmpty Method: Return a Boolean indicating whether the hash table is empty.
  Put Method: Add a new key-value pair to the table.
  Get Method: Retrieve the value associated with a given key.
  Remove Method: Remove the key-value pair associated with a given key.
  Resize Method: Double the capacity of the table and rehash all existing entries when the load factor exceeds a threshold.
