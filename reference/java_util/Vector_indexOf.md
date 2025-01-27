#### indexOf

```
public int indexOf(Object o,
                   int index)
```
Returns the index of the first occurrence of the specified element in
this vector, searching forwards from `index`, or returns -1 if
the element is not found.
More formally, returns the lowest index `i` such that
(i >= index && (o==null ? get(i)==null : o.equals(get(i)))),
or -1 if there is no such index.
Parameters:
`o` - element to search for
`index` - index to start searching from
Returns:
the index of the first occurrence of the element in
this vector at position `index` or later in the vector;
`-1` if the element is not found.
Throws:
`IndexOutOfBoundsException` - if the specified index is negative
See Also:
`Object.equals(Object)`

