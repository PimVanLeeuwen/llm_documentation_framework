#### mapping

```
public static <T,U,A,R> Collector<T,?,R> mapping(Function<? super T,? extends U> mapper,
                                                 Collector<? super U,A,R> downstream)
```
Adapts a `Collector` accepting elements of type `U` to one
accepting elements of type `T` by applying a mapping function to
each input element before accumulation.
API Note:
The `mapping()` collectors are most useful when used in a
multi-level reduction, such as downstream of a `groupingBy` or
`partitioningBy`. For example, given a stream of
`Person`, to accumulate the set of last names in each city:
```

     Map<City, Set<String>> lastNamesByCity
         = people.stream().collect(groupingBy(Person::getCity,
                                              mapping(Person::getLastName, toSet())));
 
```

Type Parameters:
`T` - the type of the input elements
`U` - type of elements accepted by downstream collector
`A` - intermediate accumulation type of the downstream collector
`R` - result type of collector
Parameters:
`mapper` - a function to be applied to the input elements
`downstream` - a collector which will accept mapped values
Returns:
a collector which applies the mapping function to the input
elements and provides the mapped results to the downstream collector

