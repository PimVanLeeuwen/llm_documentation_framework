#### remove

```
boolean remove(Object o)
```
Removes a single instance of the specified element from this queue,
if it is present. More formally, removes an element `e` such
that `o.equals(e)`, if this queue contains one or more such
elements.
Returns `true` if this queue contained the specified element
(or equivalently, if this queue changed as a result of the call).
Specified by:
`remove` in interface `Collection<E>`
Parameters:
`o` - element to be removed from this queue, if present
Returns:
`true` if this queue changed as a result of the call
Throws:
`ClassCastException` - if the class of the specified element
is incompatible with this queue
(optional)
`NullPointerException` - if the specified element is null
(optional)

