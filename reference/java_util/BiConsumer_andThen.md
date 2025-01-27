#### andThen

```
default BiConsumer<T,U> andThen(BiConsumer<? super T,? super U> after)
```
Returns a composed `BiConsumer` that performs, in sequence, this
operation followed by the `after` operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the `after` operation will not be performed.
Parameters:
`after` - the operation to perform after this operation
Returns:
a composed `BiConsumer` that performs in sequence this
operation followed by the `after` operation
Throws:
`NullPointerException` - if `after` is null




