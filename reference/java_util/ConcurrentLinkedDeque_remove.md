#### remove

```
public boolean remove(Object o)
```
Removes the first element `e` such that
`o.equals(e)`, if such an element exists in this deque.
If the deque does not contain the element, it is unchanged.
Specified by:
`remove` in interface `Collection<E>`
Specified by:
`remove` in interface `Deque<E>`
Overrides:
`remove` in class `AbstractCollection<E>`
Parameters:
`o` - element to be removed from this deque, if present
Returns:
`true` if the deque contained the specified element
Throws:
`NullPointerException` - if the specified element is null

