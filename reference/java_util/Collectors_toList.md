#### toList

```
public static <T> Collector<T,?,List<T>> toList()
```
Returns a `Collector` that accumulates the input elements into a
new `List`. There are no guarantees on the type, mutability,
serializability, or thread-safety of the `List` returned; if more
control over the returned `List` is required, use `toCollection(Supplier)`.
Type Parameters:
`T` - the type of the input elements
Returns:
a `Collector` which collects all the input elements into a
`List`, in encounter order

