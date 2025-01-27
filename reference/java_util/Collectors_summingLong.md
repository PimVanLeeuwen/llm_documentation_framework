#### summingLong

```
public static <T> Collector<T,?,Long> summingLong(ToLongFunction<? super T> mapper)
```
Returns a `Collector` that produces the sum of a long-valued
function applied to the input elements. If no elements are present,
the result is 0.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - a function extracting the property to be summed
Returns:
a `Collector` that produces the sum of a derived property

