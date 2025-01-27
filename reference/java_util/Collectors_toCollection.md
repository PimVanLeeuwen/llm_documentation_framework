#### toCollection

```
public static <T,C extends Collection<T>> Collector<T,?,C> toCollection(Supplier<C> collectionFactory)
```
Returns a `Collector` that accumulates the input elements into a
new `Collection`, in encounter order. The `Collection` is
created by the provided factory.
Type Parameters:
`T` - the type of the input elements
`C` - the type of the resulting `Collection`
Parameters:
`collectionFactory` - a `Supplier` which returns a new, empty
`Collection` of the appropriate type
Returns:
a `Collector` which collects all the input elements into a
`Collection`, in encounter order

