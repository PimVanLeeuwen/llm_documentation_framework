#### set

```
void set(E e)
```
Replaces the last element returned by `next()` or
`previous()` with the specified element (optional operation).
This call can be made only if neither `remove()` nor `add(E)` have been called after the last call to `next` or
`previous`.
Parameters:
`e` - the element with which to replace the last element returned by
`next` or `previous`
Throws:
`UnsupportedOperationException` - if the `set` operation
is not supported by this list iterator
`ClassCastException` - if the class of the specified element
prevents it from being added to this list
`IllegalArgumentException` - if some aspect of the specified
element prevents it from being added to this list
`IllegalStateException` - if neither `next` nor
`previous` have been called, or `remove` or
`add` have been called after the last call to
`next` or `previous`

