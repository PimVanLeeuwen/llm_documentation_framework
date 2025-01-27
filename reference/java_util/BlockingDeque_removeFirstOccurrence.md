#### removeFirstOccurrence

```
boolean removeFirstOccurrence(Object o)
```
Removes the first occurrence of the specified element from this deque.
If the deque does not contain the element, it is unchanged.
More formally, removes the first element `e` such that
`o.equals(e)` (if such an element exists).
Returns `true` if this deque contained the specified element
(or equivalently, if this deque changed as a result of the call).
Specified by:
`removeFirstOccurrence` in interface `Deque<E>`
Parameters:
`o` - element to be removed from this deque, if present
Returns:
`true` if an element was removed as a result of this call
Throws:
`ClassCastException` - if the class of the specified element
is incompatible with this deque
(optional)
`NullPointerException` - if the specified element is null
(optional)

