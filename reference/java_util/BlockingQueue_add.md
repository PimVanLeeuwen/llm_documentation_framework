#### add

```
boolean add(E e)
```
Inserts the specified element into this queue if it is possible to do
so immediately without violating capacity restrictions, returning
`true` upon success and throwing an
`IllegalStateException` if no space is currently available.
When using a capacity-restricted queue, it is generally preferable to
use `offer`.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `Queue<E>`
Parameters:
`e` - the element to add
Returns:
`true` (as specified by `Collection.add(E)`)
Throws:
`IllegalStateException` - if the element cannot be added at this
time due to capacity restrictions
`ClassCastException` - if the class of the specified element
prevents it from being added to this queue
`NullPointerException` - if the specified element is null
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this queue

