#### higher

```
public E higher(E e)
```
Description copied from interface: `NavigableSet`
Returns the least element in this set strictly greater than the
given element, or `null` if there is no such element.
Specified by:
`higher` in interface `NavigableSet<E>`
Parameters:
`e` - the value to match
Returns:
the least element greater than `e`,
or `null` if there is no such element
Throws:
`ClassCastException` - if the specified element cannot be
compared with the elements currently in the set
`NullPointerException` - if the specified element is null

