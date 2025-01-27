#### add

```
public boolean add(E e)
```
Inserts the specified element at the end of this deque unless it would
violate capacity restrictions. When using a capacity-restricted deque,
it is generally preferable to use method `offer`.This method is equivalent to `addLast(E)`.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `BlockingDeque<E>`
Specified by:
`add` in interface `BlockingQueue<E>`
Specified by:
`add` in interface `Deque<E>`
Specified by:
`add` in interface `Queue<E>`
Overrides:
`add` in class `AbstractQueue<E>`
Parameters:
`e` - the element to add
Returns:
true (as specified by `Collection.add(E)`)
Throws:
`IllegalStateException` - if this deque is full
`NullPointerException` - if the specified element is null

