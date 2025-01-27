#### longStream

```
public static LongStream longStream(Supplier<? extends Spliterator.OfLong> supplier,
                                    int characteristics,
                                    boolean parallel)
```
Creates a new sequential or parallel `LongStream` from a
`Supplier` of `Spliterator.OfLong`.The `Supplier.get()` method will be invoked on the supplier no
more than once, and only after the terminal operation of the stream pipeline
commences.For spliterators that report a characteristic of `IMMUTABLE`
or `CONCURRENT`, or that are
late-binding, it is likely
more efficient to use `longStream(java.util.Spliterator.OfLong, boolean)`
instead.The use of a `Supplier` in this form provides a level of
indirection that reduces the scope of potential interference with the
source. Since the supplier is only invoked after the terminal operation
commences, any modifications to the source up to the start of the
terminal operation are reflected in the stream result. See
Non-Interference for
more details.
Parameters:
`supplier` - a `Supplier` of a `Spliterator.OfLong`
`characteristics` - Spliterator characteristics of the supplied
`Spliterator.OfLong`. The characteristics must be equal to
`supplier.get().characteristics()`, otherwise undefined
behavior may occur when terminal operation commences.
`parallel` - if `true` then the returned stream is a parallel
stream; if `false` the returned stream is a sequential
stream.
Returns:
a new sequential or parallel `LongStream`
See Also:
`longStream(java.util.Spliterator.OfLong, boolean)`

