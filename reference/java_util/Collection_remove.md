#### remove

```
boolean remove(Object o)
```
Removes a single instance of the specified element from this
collection, if it is present (optional operation). More formally,
removes an element e such that
(o==null ? e==null : o.equals(e)), if
this collection contains one or more such elements. Returns
true if this collection contained the specified element (or
equivalently, if this collection changed as a result of the call).
Parameters:
`o` - element to be removed from this collection, if present
Returns:
true if an element was removed as a result of this call
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this collection
(optional)
`NullPointerException` - if the specified element is null and this
collection does not permit null elements
(optional)
`UnsupportedOperationException` - if the remove operation
is not supported by this collection

