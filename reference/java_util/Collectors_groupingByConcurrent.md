#### groupingByConcurrent

```
public static <T,K,A,D,M extends ConcurrentMap<K,D>> Collector<T,?,M> groupingByConcurrent(Function<? super T,? extends K> classifier,
                                                                                           Supplier<M> mapFactory,
                                                                                           Collector<? super T,A,D> downstream)
```
Returns a concurrent `Collector` implementing a cascaded "group by"
operation on input elements of type `T`, grouping elements
according to a classification function, and then performing a reduction
operation on the values associated with a given key using the specified
downstream `Collector`. The `ConcurrentMap` produced by the
Collector is created with the supplied factory function.This is a `concurrent` and
`unordered` Collector.The classification function maps elements to some key type `K`.
The downstream collector operates on elements of type `T` and
produces a result of type `D`. The resulting collector produces a
`Map<K, D>`.For example, to compute the set of last names of people in each city,
where the city names are sorted:
```

     ConcurrentMap<City, Set<String>> namesByCity
         = people.stream().collect(groupingBy(Person::getCity, ConcurrentSkipListMap::new,
                                              mapping(Person::getLastName, toSet())));
 
```

Type Parameters:
`T` - the type of the input elements
`K` - the type of the keys
`A` - the intermediate accumulation type of the downstream collector
`D` - the result type of the downstream reduction
`M` - the type of the resulting `ConcurrentMap`
Parameters:
`classifier` - a classifier function mapping input elements to keys
`downstream` - a `Collector` implementing the downstream reduction
`mapFactory` - a function which, when called, produces a new empty
`ConcurrentMap` of the desired type
Returns:
a concurrent, unordered `Collector` implementing the cascaded group-by operation
See Also:
`groupingByConcurrent(Function)`,
`groupingByConcurrent(Function, Collector)`,
`groupingBy(Function, Supplier, Collector)`

