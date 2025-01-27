#### stream

```
default Stream<E> stream()
```
Returns a sequential `Stream` with this collection as its source.This method should be overridden when the `spliterator()`
method cannot return a spliterator that is `IMMUTABLE`,
`CONCURRENT`, or late-binding. (See `spliterator()`
for details.)
Implementation Requirements:
The default implementation creates a sequential `Stream` from the
collection's `Spliterator`.
Returns:
a sequential `Stream` over the elements in this collection
Since:
1.8

