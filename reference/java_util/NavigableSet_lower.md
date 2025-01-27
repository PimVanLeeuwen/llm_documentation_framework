#### lower

```
E lower(E e)
```
Returns the greatest element in this set strictly less than the
given element, or `null` if there is no such element.
Parameters:
`e` - the value to match
Returns:
the greatest element less than `e`,
or `null` if there is no such element
Throws:
`ClassCastException` - if the specified element cannot be
compared with the elements currently in the set
`NullPointerException` - if the specified element is null
and this set does not permit null elements

