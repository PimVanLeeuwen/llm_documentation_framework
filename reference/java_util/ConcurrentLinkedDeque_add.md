#### add

```
public boolean add(E e)
```
Inserts the specified element at the tail of this deque.
As the deque is unbounded, this method will never throw
`IllegalStateException` or return `false`.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `Deque<E>`
Specified by:
`add` in interface `Queue<E>`
Overrides:
`add` in class `AbstractCollection<E>`
Parameters:
`e` - element whose presence in this collection is to be ensured
Returns:
`true` (as specified by `Collection.add(E)`)
Throws:
`NullPointerException` - if the specified element is null

