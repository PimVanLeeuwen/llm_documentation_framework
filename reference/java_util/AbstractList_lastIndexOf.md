#### lastIndexOf

```
public int lastIndexOf(Object o)
```
Returns the index of the last occurrence of the specified element
in this list, or -1 if this list does not contain the element.
More formally, returns the highest index i such that
(o==null ? get(i)==null : o.equals(get(i))),
or -1 if there is no such index.This implementation first gets a list iterator that points to the end
of the list (with `listIterator(size())`). Then, it iterates
backwards over the list until the specified element is found, or the
beginning of the list is reached.
Specified by:
`lastIndexOf` in interface `List<E>`
Parameters:
`o` - element to search for
Returns:
the index of the last occurrence of the specified element in
this list, or -1 if this list does not contain the element
Throws:
`ClassCastException` - if the type of the specified element
is incompatible with this list
(optional)
`NullPointerException` - if the specified element is null and this
list does not permit null elements
(optional)

