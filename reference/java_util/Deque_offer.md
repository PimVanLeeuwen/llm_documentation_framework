#### offer

```
boolean offer(E e)
```
Inserts the specified element into the queue represented by this deque
(in other words, at the tail of this deque) if it is possible to do so
immediately without violating capacity restrictions, returning
`true` upon success and `false` if no space is currently
available. When using a capacity-restricted deque, this method is
generally preferable to the `add(E)` method, which can fail to
insert an element only by throwing an exception.This method is equivalent to `offerLast(E)`.
Specified by:
`offer` in interface `Queue<E>`
Parameters:
`e` - the element to add
Returns:
`true` if the element was added to this deque, else
`false`
Throws:
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null and this
deque does not permit null elements
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

