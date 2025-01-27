#### parallel

```
DoubleStream parallel()
```
Description copied from interface: `BaseStream`
Returns an equivalent stream that is parallel. May return
itself, either because the stream was already parallel, or because
the underlying stream state was modified to be parallel.This is an intermediate
operation.
Specified by:
`parallel` in interface `BaseStream<Double,DoubleStream>`
Returns:
a parallel stream

