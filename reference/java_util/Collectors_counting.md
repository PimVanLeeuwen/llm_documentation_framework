#### counting

```
public static <T> Collector<T,?,Long> counting()
```
Returns a `Collector` accepting elements of type `T` that
counts the number of input elements. If no elements are present, the
result is 0.
Implementation Requirements:
This produces a result equivalent to:
```

     reducing(0L, e -> 1L, Long::sum)
 
```

Type Parameters:
`T` - the type of the input elements
Returns:
a `Collector` that counts the input elements

