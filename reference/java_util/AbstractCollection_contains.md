#### contains

```
public boolean contains(Object o)
```
Returns true if this collection contains the specified element.
More formally, returns true if and only if this collection
contains at least one element e such that
(o==null ? e==null : o.equals(e)).This implementation iterates over the elements in the collection,
checking each element in turn for equality with the specified element.
Specified by:
`contains` in interface `Collection<E>`
Parameters:
`o` - element whose presence in this collection is to be tested
Returns:
true if this collection contains the specified
element
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this collection
(optional)
`NullPointerException` - if the specified element is null and this
collection does not permit null elements
(optional)

