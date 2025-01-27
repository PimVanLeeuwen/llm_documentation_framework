#### ceiling

```
public E ceiling(E e)
```
Description copied from interface: `NavigableSet`
Returns the least element in this set greater than or equal to
the given element, or `null` if there is no such element.
Specified by:
`ceiling` in interface `NavigableSet<E>`
Parameters:
`e` - the value to match
Returns:
the least element greater than or equal to `e`,
or `null` if there is no such element
Throws:
`ClassCastException` - if the specified element cannot be
compared with the elements currently in the set
`NullPointerException` - if the specified element is null

