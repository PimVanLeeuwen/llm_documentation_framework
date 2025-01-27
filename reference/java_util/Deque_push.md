#### push

```
void push(E e)
```
Pushes an element onto the stack represented by this deque (in other
words, at the head of this deque) if it is possible to do so
immediately without violating capacity restrictions, throwing an
`IllegalStateException` if no space is currently available.This method is equivalent to `addFirst(E)`.
Parameters:
`e` - the element to push
Throws:
`IllegalStateException` - if the element cannot be added at this
time due to capacity restrictions
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null and this
deque does not permit null elements
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

