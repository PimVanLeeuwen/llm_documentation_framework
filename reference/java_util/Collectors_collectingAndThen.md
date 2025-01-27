#### collectingAndThen

```
public static <T,A,R,RR> Collector<T,A,RR> collectingAndThen(Collector<T,A,R> downstream,
                                                             Function<R,RR> finisher)
```
Adapts a `Collector` to perform an additional finishing
transformation. For example, one could adapt the `toList()`
collector to always produce an immutable list with:
```

     List<String> people
         = people.stream().collect(collectingAndThen(toList(), Collections::unmodifiableList));
 
```

Type Parameters:
`T` - the type of the input elements
`A` - intermediate accumulation type of the downstream collector
`R` - result type of the downstream collector
`RR` - result type of the resulting collector
Parameters:
`downstream` - a collector
`finisher` - a function to be applied to the final result of the downstream collector
Returns:
a collector which performs the action of the downstream collector,
followed by an additional finishing step

