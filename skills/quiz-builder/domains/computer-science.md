# Domain Pack: Computer Science

Scenarios for a computer-science course. The student reasons about data structures, algorithms, complexity, and program behavior, and avoids the classic bugs and misconceptions.

## Scenario entities and decisions

- A program that has to pick the right data structure for an access pattern.
- A function whose time or space complexity has to be judged.
- A snippet with a bug to diagnose (off-by-one, missing base case, wrong comparison).
- A design choice between two correct approaches with different tradeoffs.

## Concepts and vocabulary (with realistic framing)

- Complexity: Big-O for time and space, best, average, and worst case, common classes (constant, logarithmic, linear, linearithmic, quadratic, exponential).
- Data structures: array, linked list, stack, queue, hash table, binary search tree, heap, graph, and the operations each makes fast or slow.
- Programming concepts: recursion and the base case, iteration versus recursion, the call stack, pass by value versus by reference, mutability, scope, encapsulation, inheritance, polymorphism, compile-time versus runtime errors, Boolean logic.

## What good distractors look like here

- Quoting average-case complexity where the worst case is asked, or treating a hash-table lookup as always constant time while ignoring collisions.
- Off-by-one errors in loop bounds or array indexing.
- Confusing assignment with comparison, or equality of value with identity of reference.
- A recursion with no base case, or one that does not move toward it.
- Confusing a compile-time error (type, syntax) with a runtime error (null reference, divide by zero).
- Picking a data structure that is correct but slow for the access pattern (a list where a hash table is needed for lookup).

## House style: two worked examples

Scenario, medium: "A program looks up user records thousands of times by exact id, with rare inserts. Which structure gives the best average lookup, and what is the catch?" Correct answer: a hash table gives average constant-time lookup; the catch is that worst-case lookup degrades toward linear under many collisions or poor hashing. Distractors: a sorted array (logarithmic lookup but slow inserts), a linked list (linear lookup), a binary tree without noting balance.

Scenario, medium: "A recursive function to sum a list calls itself on the rest of the list but never checks for the empty list. What happens, and what fixes it?" Correct answer: it recurses without stopping and overflows the call stack; adding a base case (return 0 for the empty list) fixes it. Distractors: it returns the wrong sum, it is a compile error, it is fine because recursion always terminates.

## Feedback voice

Correct-answer feedback names the concept (the complexity class, the structure's tradeoff, the base case). Incorrect-answer feedback names the bug or misconception, for example average versus worst case or value versus reference, without restating the answer.
