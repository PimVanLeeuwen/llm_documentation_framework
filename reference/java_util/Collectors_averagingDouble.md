#### averagingDouble

```
public static <T> Collector<T,?,Double> averagingDouble(ToDoubleFunction<? super T> mapper)
```
Returns a `Collector` that produces the arithmetic mean of a double-valued
function applied to the input elements. If no elements are present,
the result is 0.The average returned can vary depending upon the order in which
values are recorded, due to accumulated rounding error in
addition of values of differing magnitudes. Values sorted by increasing
absolute magnitude tend to yield more accurate results. If any recorded
value is a `NaN` or the sum is at any point a `NaN` then the
average will be `NaN`.
Implementation Note:
The `double` format can represent all
consecutive integers in the range -253 to
253. If the pipeline has more than 253
values, the divisor in the average computation will saturate at
253, leading to additional numerical errors.
Type Parameters:
`T` - the type of the input elements
Parameters:
`mapper` - a function extracting the property to be summed
Returns:
a `Collector` that produces the sum of a derived property

