#### contains

```
boolean contains(Object o)
```
Returns `true` if this deque contains the specified element.
More formally, returns `true` if and only if this deque contains
at least one element `e` such that `o.equals(e)`.
Specified by:
`contains` in interface `BlockingQueue<E>`
Specified by:
`contains` in interface `Collection<E>`
Specified by:
`contains` in interface `Deque<E>`
Parameters:
`o` - object to be checked for containment in this deque
Returns:
`true` if this deque contains the specified element
Throws:
`ClassCastException` - if the class of the specified element
is incompatible with this deque
(optional)
`NullPointerException` - if the specified element is null
(optional)

