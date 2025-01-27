#### distinct

```
Stream<T> distinct()
```
Returns a stream consisting of the distinct elements (according to
`Object.equals(Object)`) of this stream.For ordered streams, the selection of distinct elements is stable
(for duplicated elements, the element appearing first in the encounter
order is preserved.) For unordered streams, no stability guarantees
are made.This is a stateful
intermediate operation.
API Note:
Preserving stability for `distinct()` in parallel pipelines is
relatively expensive (requires that the operation act as a full barrier,
with substantial buffering overhead), and stability is often not needed.
Using an unordered stream source (such as `generate(Supplier)`)
or removing the ordering constraint with `BaseStream.unordered()` may result
in significantly more efficient execution for `distinct()` in parallel
pipelines, if the semantics of your situation permit. If consistency
with encounter order is required, and you are experiencing poor performance
or memory utilization with `distinct()` in parallel pipelines,
switching to sequential execution with `BaseStream.sequential()` may improve
performance.
Returns:
the new stream

