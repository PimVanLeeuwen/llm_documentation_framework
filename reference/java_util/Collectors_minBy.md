#### minBy

```
public static <T> Collector<T,?,Optional<T>> minBy(Comparator<? super T> comparator)
```
Returns a `Collector` that produces the minimal element according
to a given `Comparator`, described as an `Optional<T>`.
Implementation Requirements:
This produces a result equivalent to:
```

     reducing(BinaryOperator.minBy(comparator))
 
```

Type Parameters:
`T` - the type of the input elements
Parameters:
`comparator` - a `Comparator` for comparing elements
Returns:
a `Collector` that produces the minimal value

