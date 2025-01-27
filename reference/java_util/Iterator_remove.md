#### remove

```
default void remove()
```
Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to `next()`. The behavior of an iterator
is unspecified if the underlying collection is modified while the
iteration is in progress in any way other than by calling this
method.
Implementation Requirements:
The default implementation throws an instance of
`UnsupportedOperationException` and performs no other action.
Throws:
`UnsupportedOperationException` - if the `remove`
operation is not supported by this iterator
`IllegalStateException` - if the `next` method has not
yet been called, or the `remove` method has already
been called after the last call to the `next`
method

