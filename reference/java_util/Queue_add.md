#### add

```
boolean add(E e)
```
Inserts the specified element into this queue if it is possible to do so
immediately without violating capacity restrictions, returning
`true` upon success and throwing an `IllegalStateException`
if no space is currently available.
Specified by:
`add` in interface `Collection<E>`
Parameters:
`e` - the element to add
Returns:
`true` (as specified by `Collection.add(E)`)
Throws:
`IllegalStateException` - if the element cannot be added at this
time due to capacity restrictions
`ClassCastException` - if the class of the specified element
prevents it from being added to this queue
`NullPointerException` - if the specified element is null and
this queue does not permit null elements
`IllegalArgumentException` - if some property of this element
prevents it from being added to this queue

