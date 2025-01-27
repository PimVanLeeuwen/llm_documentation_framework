#### contains

```
boolean contains(Object o)
```
Returns true if this set contains the specified element.
More formally, returns true if and only if this set
contains an element e such that
(o==null ? e==null : o.equals(e)).
Specified by:
`contains` in interface `Collection<E>`
Parameters:
`o` - element whose presence in this set is to be tested
Returns:
true if this set contains the specified element
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this set
(optional)
`NullPointerException` - if the specified element is null and this
set does not permit null elements
(optional)

