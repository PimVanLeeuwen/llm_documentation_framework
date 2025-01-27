#### add

```
boolean add(E e)
```
Adds the specified element to this set if it is not already present
(optional operation). More formally, adds the specified element
e to this set if the set contains no element e2
such that
(e==null ? e2==null : e.equals(e2)).
If this set already contains the element, the call leaves the set
unchanged and returns false. In combination with the
restriction on constructors, this ensures that sets never contain
duplicate elements.The stipulation above does not imply that sets must accept all
elements; sets may refuse to add any particular element, including
null, and throw an exception, as described in the
specification for `Collection.add`.
Individual set implementations should clearly document any
restrictions on the elements that they may contain.
Specified by:
`add` in interface `Collection<E>`
Parameters:
`e` - element to be added to this set
Returns:
true if this set did not already contain the specified
element
Throws:
`UnsupportedOperationException` - if the add operation
is not supported by this set
`ClassCastException` - if the class of the specified element
prevents it from being added to this set
`NullPointerException` - if the specified element is null and this
set does not permit null elements
`IllegalArgumentException` - if some property of the specified element
prevents it from being added to this set

