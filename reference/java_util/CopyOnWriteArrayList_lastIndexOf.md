#### lastIndexOf

```
public int lastIndexOf(E e,
                       int index)
```
Returns the index of the last occurrence of the specified element in
this list, searching backwards from `index`, or returns -1 if
the element is not found.
More formally, returns the highest index `i` such that
(i <= index && (e==null ? get(i)==null : e.equals(get(i)))),
or -1 if there is no such index.
Parameters:
`e` - element to search for
`index` - index to start searching backwards from
Returns:
the index of the last occurrence of the element at position
less than or equal to `index` in this list;
-1 if the element is not found.
Throws:
`IndexOutOfBoundsException` - if the specified index is greater
than or equal to the current size of this list

