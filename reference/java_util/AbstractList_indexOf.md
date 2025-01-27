#### indexOf

```
public int indexOf(Object o)
```
Returns the index of the first occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the lowest index i such that
(o==null ? get(i)==null : o.equals(get(i))),
or -1 if there is no such index.This implementation first gets a list iterator (with
`listIterator()`). Then, it iterates over the list until the
specified element is found or the end of the list is reached.
Specified by:
`indexOf` in interface `List<E>`
Parameters:
`o` - element to search for
Returns:
the index of the first occurrence of the specified element in
this list, or -1 if this list does not contain the element
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this list
(optional)
`NullPointerException` - if the specified element is null and this
list does not permit null elements
(optional)

