#### flatMapToDouble

```
DoubleStream flatMapToDouble(Function<? super T,? extends DoubleStream> mapper)
```
Returns an `DoubleStream` consisting of the results of replacing
each element of this stream with the contents of a mapped stream produced
by applying the provided mapping function to each element. Each mapped
stream is `closed` after its
contents have placed been into this stream. (If a mapped stream is
`null` an empty stream is used, instead.)This is an intermediate
operation.
Parameters:
`mapper` - a non-interfering,
stateless
function to apply to each element which produces a stream
of new values
Returns:
the new stream
See Also:
`flatMap(Function)`

