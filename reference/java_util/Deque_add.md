#### add

```
boolean add(E e)
```
Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning
`true` upon success and throwing an
`IllegalStateException` if no space is currently available.
When using a capacity-restricted deque, it is generally preferable to
use `offer`.This method is equivalent to `addLast(E)`.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `Queue<E>`
Parameters:
`e` - the element to add
Returns:
`true` (as specified by `Collection.add(E)`)
Throws:
`IllegalStateException` - if the element cannot be added at this
time due to capacity restrictions
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null and this
deque does not permit null elements
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

