#### previous

```
E previous()
```
Returns the previous element in the list and moves the cursor
position backwards. This method may be called repeatedly to
iterate through the list backwards, or intermixed with calls to
`next()` to go back and forth. (Note that alternating calls
to `next` and `previous` will return the same
element repeatedly.)
Returns:
the previous element in the list
Throws:
`NoSuchElementException` - if the iteration has no previous
element

