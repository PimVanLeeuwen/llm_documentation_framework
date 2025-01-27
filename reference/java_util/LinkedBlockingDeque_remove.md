#### remove

```
public boolean remove(Object o)
```
Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element `e` such that
`o.equals(e)` (if such an element exists).
Returns `true` if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).This method is equivalent to
`removeFirstOccurrence`.
Specified by:
`remove` in interface `Collection<E>`
Specified by:
`remove` in interface `BlockingDeque<E>`
Specified by:
`remove` in interface `BlockingQueue<E>`
Specified by:
`remove` in interface `Deque<E>`
Overrides:
`remove` in class `AbstractCollection<E>`
Parameters:
`o` - element to be removed from this deque, if present
Returns:
`true` if this deque changed as a result of the call

