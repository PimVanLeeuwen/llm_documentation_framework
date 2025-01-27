#### floor

```
public E floor(E e)
```
Description copied from interface: `NavigableSet`
Returns the greatest element in this set less than or equal to
the given element, or `null` if there is no such element.
Specified by:
`floor` in interface `NavigableSet<E>`
Parameters:
`e` - the value to match
Returns:
the greatest element less than or equal to `e`,
or `null` if there is no such element
Throws:
`ClassCastException` - if the specified element cannot be
compared with the elements currently in the set
`NullPointerException` - if the specified element is null
and this set uses natural ordering, or its comparator
does not permit null elements
Since:
1.6

