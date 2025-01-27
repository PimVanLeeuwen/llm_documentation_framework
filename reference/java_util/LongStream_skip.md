#### skip

```
LongStream skip(long n)
```
Returns a stream consisting of the remaining elements of this stream
after discarding the first `n` elements of the stream.
If this stream contains fewer than `n` elements then an
empty stream will be returned.This is a stateful
intermediate operation.
API Note:
While `skip()` is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of `n`, since `skip(n)`
is constrained to skip not just any n elements, but the
first n elements in the encounter order. Using an unordered
stream source (such as `generate(LongSupplier)`) or removing the
ordering constraint with `BaseStream.unordered()` may result in significant
speedups of `skip()` in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with
`skip()` in parallel pipelines, switching to sequential execution
with `sequential()` may improve performance.
Parameters:
`n` - the number of leading elements to skip
Returns:
the new stream
Throws:
`IllegalArgumentException` - if `n` is negative

