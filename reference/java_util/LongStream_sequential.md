#### sequential

```
LongStream sequential()
```
Description copied from interface: `BaseStream`
Returns an equivalent stream that is sequential. May return
itself, either because the stream was already sequential, or because
the underlying stream state was modified to be sequential.This is an intermediate
operation.
Specified by:
`sequential` in interface `BaseStream<Long,LongStream>`
Returns:
a sequential stream

