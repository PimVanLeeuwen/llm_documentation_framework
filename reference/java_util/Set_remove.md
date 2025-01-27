#### remove

```
boolean remove(Object o)
```
Removes the specified element from this set if it is present
(optional operation). More formally, removes an element e
such that
(o==null ? e==null : o.equals(e)), if
this set contains such an element. Returns true if this set
contained the element (or equivalently, if this set changed as a
result of the call). (This set will not contain the element once the
call returns.)
Specified by:
`remove` in interface `Collection<E>`
Parameters:
`o` - object to be removed from this set, if present
Returns:
true if this set contained the specified element
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this set
(optional)
`NullPointerException` - if the specified element is null and this
set does not permit null elements
(optional)
`UnsupportedOperationException` - if the remove operation
is not supported by this set

