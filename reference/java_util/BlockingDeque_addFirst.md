#### addFirst

```
void addFirst(E e)
```
Inserts the specified element at the front of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an `IllegalStateException` if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use `offerFirst`.
Specified by:
`addFirst` in interface `Deque<E>`
Parameters:
`e` - the element to add
Throws:
`IllegalStateException` - if the element cannot be added at this
time due to capacity restrictions
`ClassCastException` - if the class of the specified element
prevents it from being added to this deque
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this deque

