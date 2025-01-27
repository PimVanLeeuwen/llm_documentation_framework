#### next

```
E next()
```
Returns the next element in the list and advances the cursor position.
This method may be called repeatedly to iterate through the list,
or intermixed with calls to `previous()` to go back and forth.
(Note that alternating calls to `next` and `previous`
will return the same element repeatedly.)
Specified by:
`next` in interface `Iterator<E>`
Returns:
the next element in the list
Throws:
`NoSuchElementException` - if the iteration has no next element

