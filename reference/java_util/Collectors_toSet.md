#### toSet

```
public static <T> Collector<T,?,Set<T>> toSet()
```
Returns a `Collector` that accumulates the input elements into a
new `Set`. There are no guarantees on the type, mutability,
serializability, or thread-safety of the `Set` returned; if more
control over the returned `Set` is required, use
`toCollection(Supplier)`.This is an `unordered`
Collector.
Type Parameters:
`T` - the type of the input elements
Returns:
a `Collector` which collects all the input elements into a
`Set`

