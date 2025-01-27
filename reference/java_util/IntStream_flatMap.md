#### flatMap

```
IntStream flatMap(IntFunction<? extends IntStream> mapper)
```
Returns a stream consisting of the results of replacing each element of
this stream with the contents of a mapped stream produced by applying
the provided mapping function to each element. Each mapped stream is
`closed` after its contents
have been placed into this stream. (If a mapped stream is `null`
an empty stream is used, instead.)This is an intermediate
operation.
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element which produces an
`IntStream` of new values
Returns:
the new stream
See Also:
`Stream.flatMap(Function)`

