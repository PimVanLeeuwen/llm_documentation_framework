#### partitioningBy

```
public static <T,D,A> Collector<T,?,Map<Boolean,D>> partitioningBy(Predicate<? super T> predicate,
                                                                   Collector<? super T,A,D> downstream)
```
Returns a `Collector` which partitions the input elements according
to a `Predicate`, reduces the values in each partition according to
another `Collector`, and organizes them into a
`Map<Boolean, D>` whose values are the result of the downstream
reduction.There are no guarantees on the type, mutability,
serializability, or thread-safety of the `Map` returned.
Type Parameters:
`T` - the type of the input elements
`A` - the intermediate accumulation type of the downstream collector
`D` - the result type of the downstream reduction
Parameters:
`predicate` - a predicate used for classifying input elements
`downstream` - a `Collector` implementing the downstream
reduction
Returns:
a `Collector` implementing the cascaded partitioning
operation
See Also:
`partitioningBy(Predicate)`

