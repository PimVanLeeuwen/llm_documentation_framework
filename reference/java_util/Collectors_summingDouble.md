#### summingDouble

```
public static <T> Collector<T,?,Double> summingDouble(ToDoubleFunction<? super T> mapper)
```
Returns a `Collector` that produces the sum of a double-valued
function applied to the input elements. If no elements are present,
the result is 0.The sum returned can vary depending upon the order in which
values are recorded, due to accumulated rounding error in
addition of values of differing magnitudes. Values sorted by increasing
absolute magnitude tend to yield more accurate results. If any recorded
value is a `NaN` or the sum is at any point a `NaN` then the
sum will be `NaN`.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - a function extracting the property to be summed
Returns:
a `Collector` that produces the sum of a derived property

