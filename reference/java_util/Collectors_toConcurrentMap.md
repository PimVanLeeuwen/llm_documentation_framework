#### toConcurrentMap

```
public static <T,K,U,M extends ConcurrentMap<K,U>> Collector<T,?,M> toConcurrentMap(Function<? super T,? extends K> keyMapper,
                                                                                    Function<? super T,? extends U> valueMapper,
                                                                                    BinaryOperator<U> mergeFunction,
                                                                                    Supplier<M> mapSupplier)
```
Returns a concurrent `Collector` that accumulates elements into a
`ConcurrentMap` whose keys and values are the result of applying
the provided mapping functions to the input elements.If the mapped keys contains duplicates (according to `Object.equals(Object)`),
the value mapping function is applied to each equal element, and the
results are merged using the provided merging function. The
`ConcurrentMap` is created by a provided supplier function.This is a `concurrent` and
`unordered` Collector.
Type Parameters:
`T` - the type of the input elements
`K` - the output type of the key mapping function
`U` - the output type of the value mapping function
`M` - the type of the resulting `ConcurrentMap`
Parameters:
`keyMapper` - a mapping function to produce keys
`valueMapper` - a mapping function to produce values
`mergeFunction` - a merge function, used to resolve collisions between
values associated with the same key, as supplied
to `Map.merge(Object, Object, BiFunction)`
`mapSupplier` - a function which returns a new, empty `Map` into
which the results will be inserted
Returns:
a concurrent, unordered `Collector` which collects elements into a
`ConcurrentMap` whose keys are the result of applying a key mapping
function to the input elements, and whose values are the result of
applying a value mapping function to all input elements equal to the key
and combining them using the merge function
See Also:
`toConcurrentMap(Function, Function)`,
`toConcurrentMap(Function, Function, BinaryOperator)`,
`toMap(Function, Function, BinaryOperator, Supplier)`

