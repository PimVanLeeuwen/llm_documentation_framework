#### addLast

```
public void addLast(E e)
```
Description copied from interface: `BlockingDeque`
Inserts the specified element at the end of this deque if it is
possible to do so immediately without violating capacity restrictions,
throwing an `IllegalStateException` if no space is currently
available. When using a capacity-restricted deque, it is generally
preferable to use `offerLast`.
Specified by:
`addLast` in interface `BlockingDeque<E>`
Specified by:
`addLast` in interface `Deque<E>`
Parameters:
`e` - the element to add
Throws:
`IllegalStateException` - if this deque is full
`NullPointerException` - if the specified element is null

