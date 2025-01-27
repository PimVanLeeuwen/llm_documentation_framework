#### averagingInt

```
public static <T> Collector<T,?,Double> averagingInt(ToIntFunction<? super T> mapper)
```
Returns a `Collector` that produces the arithmetic mean of an integer-valued
function applied to the input elements. If no elements are present,
the result is 0.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - a function extracting the property to be summed
Returns:
a `Collector` that produces the sum of a derived property

