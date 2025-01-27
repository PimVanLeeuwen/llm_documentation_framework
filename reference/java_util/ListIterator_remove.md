#### remove

```
void remove()
```
Removes from the list the last element that was returned by `next()` or `previous()` (optional operation). This call can
only be made once per call to `next` or `previous`.
It can be made only if `add(E)` has not been
called after the last call to `next` or `previous`.
Specified by:
`remove` in interface `Iterator<E>`
Throws:
`UnsupportedOperationException` - if the `remove`
operation is not supported by this list iterator
`IllegalStateException` - if neither `next` nor
`previous` have been called, or `remove` or
`add` have been called after the last call to
`next` or `previous`

