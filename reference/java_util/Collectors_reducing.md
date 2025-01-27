#### reducing

```
public static <T,U> Collector<T,?,U> reducing(U identity,
                                              Function<? super T,? extends U> mapper,
                                              BinaryOperator<U> op)
```
Returns a `Collector` which performs a reduction of its
input elements under a specified mapping function and
`BinaryOperator`. This is a generalization of
`reducing(Object, BinaryOperator)` which allows a transformation
of the elements before reduction.
API Note:
The `reducing()` collectors are most useful when used in a
multi-level reduction, downstream of `groupingBy` or
`partitioningBy`. To perform a simple map-reduce on a stream,
use `Stream.map(Function)` and `Stream.reduce(Object, BinaryOperator)`
instead.For example, given a stream of `Person`, to calculate the longest
last name of residents in each city:
```

     Comparator<String> byLength = Comparator.comparing(String::length);
     Map<City, String> longestLastNameByCity
         = people.stream().collect(groupingBy(Person::getCity,
                                              reducing(Person::getLastName, BinaryOperator.maxBy(byLength))));
 
```

Type Parameters:
`T` - the type of the input elements
`U` - the type of the mapped values
Parameters:
`identity` - the identity value for the reduction (also, the value
that is returned when there are no input elements)
`mapper` - a mapping function to apply to each input value
`op` - a `BinaryOperator<U>` used to reduce the mapped values
Returns:
a `Collector` implementing the map-reduce operation
See Also:
`reducing(Object, BinaryOperator)`,
`reducing(BinaryOperator)`

