#### headSet

```
SortedSet<E> headSet(E toElement)
```
Returns a view of the portion of this set whose elements are
strictly less than toElement. The returned set is
backed by this set, so changes in the returned set are
reflected in this set, and vice-versa. The returned set
supports all optional set operations that this set supports.The returned set will throw an IllegalArgumentException
on an attempt to insert an element outside its range.Equivalent to `headSet(toElement, false)`.
Specified by:
`headSet` in interface `SortedSet<E>`
Parameters:
`toElement` - high endpoint (exclusive) of the returned set
Returns:
a view of the portion of this set whose elements are strictly
less than toElement
Throws:
`ClassCastException` - if toElement is not compatible
with this set's comparator (or, if the set has no comparator,
if toElement does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if toElement cannot be compared to elements
currently in the set.
`NullPointerException` - if toElement is null and
this set does not permit null elements
`IllegalArgumentException` - if this set itself has a
restricted range, and toElement lies outside the
bounds of the range

