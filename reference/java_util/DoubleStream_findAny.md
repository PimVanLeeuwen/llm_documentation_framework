#### findAny

```
OptionalDouble findAny()
```
Returns an `OptionalDouble` describing some element of the stream,
or an empty `OptionalDouble` if the stream is empty.This is a short-circuiting
terminal operation.The behavior of this operation is explicitly nondeterministic; it is
free to select any element in the stream. This is to allow for maximal
performance in parallel operations; the cost is that multiple invocations
on the same source may not return the same result. (If a stable result
is desired, use `findFirst()` instead.)
Returns:
an `OptionalDouble` describing some element of this stream,
or an empty `OptionalDouble` if the stream is empty
See Also:
`findFirst()`

