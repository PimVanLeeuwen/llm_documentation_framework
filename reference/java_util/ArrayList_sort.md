#### sort

```
public void sort(Comparator<? super E> c)
```
Description copied from interface: `List`
Sorts this list according to the order induced by the specified
`Comparator`.All elements in this list must be mutually comparable using the
specified comparator (that is, `c.compare(e1, e2)` must not throw
a `ClassCastException` for any elements `e1` and `e2`
in the list).If the specified comparator is `null` then all elements in this
list must implement the `Comparable` interface and the elements'
natural ordering should be used.This list must be modifiable, but need not be resizable.
Specified by:
`sort` in interface `List<E>`
Parameters:
`c` - the `Comparator` used to compare list elements.
A `null` value indicates that the elements'
natural ordering should be used




