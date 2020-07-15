Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(1)
2. What is the runtime complexity of `push` using a linked list?
O(1)
3. What is the runtime complexity of `pop` using a list?
O(1) assuming we pop last elelment, else O(n)
4. What is the runtime complexity of `pop` using a linked list?
O(1) assume we have pointer to last element, else O(n)
5. What is the runtime complexity of `len` using a list?
O(1)
6. What is the runtime complexity of `len` using a linked list?
O(1)
## Queue

1. What is the runtime complexity of `enqueue` using a list?
O(1)
2. What is the runtime complexity of `enqueue` using a linked list?
O(1)
3. What is the runtime complexity of `dequeue` using a list?
O(n) we have to shift each element when dequeueing
4. What is the runtime complexity of `dequeue` using a linked list?
O(1)
5. What is the runtime complexity of `len` using a list?
O(1)
6. What is the runtime complexity of `len` using a linked list?
O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
O(1)
3. What is the runtime complexity of `ListNode.delete`?
O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Not sure about JS, but can look this up and get back with an answer when I'm finished in the rest of the project.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(h) where h is the height of the tree
O(n) worst case, unbalanced tree, if balanced tree: O(log(n)) 
2. What is the runtime complexity of `contains`?
O(h) where h is the height of the tree
O(n) is worst case unbalanced tree, if balanced tree: O(log(n))
3. What is the runtime complexity of `get_max`? 
O(h) where h is the height of the tree
O(n) is worst case unbalanced tree, if balanced tree: O(log(n))
4. What is the runtime complexity of `for_each`?
O(n), you must iterate through each element
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
