#### limit

```
DoubleStream limit(long maxSize)
```
Returns a stream consisting of the elements of this stream, truncated
to be no longer than `maxSize` in length.This is a short-circuiting
stateful intermediate operation.
API Note:
While `limit()` is generally a cheap operation on sequential
stream pipelines, it can be quite expensive on ordered parallel pipelines,
especially for large values of `maxSize`, since `limit(n)`
is constrained to return not just any n elements, but the
first n elements in the encounter order. Using an unordered
stream source (such as `generate(DoubleSupplier)`) or removing the
ordering constraint with `BaseStream.unordered()` may result in significant
speedups of `limit()` in parallel pipelines, if the semantics of
your situation permit. If consistency with encounter order is required,
and you are experiencing poor performance or memory utilization with
`limit()` in parallel pipelines, switching to sequential execution
with `sequential()` may improve performance.
Parameters:
`maxSize` - the number of elements the stream should be limited to
Returns:
the new stream
Throws:
`IllegalArgumentException` - if `maxSize` is negative

