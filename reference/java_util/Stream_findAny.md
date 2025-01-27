#### findAny

```
Optional<T> findAny()
```
Returns an `Optional` describing some element of the stream, or an
empty `Optional` if the stream is empty.This is a short-circuiting
terminal operation.The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use `findFirst()` instead.)
Returns:
an `Optional` describing some element of this stream, or an
empty `Optional` if the stream is empty
Throws:
`NullPointerException` - if the element selected is null
See Also:
`findFirst()`

