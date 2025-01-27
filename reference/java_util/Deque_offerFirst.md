#### offerFirst

```
boolean offerFirst(E e)
```
Inserts the specified element at the front of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
this method is generally preferable to the `addFirst(E)` method,
which can fail to insert an element only by throwing an exception.
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

