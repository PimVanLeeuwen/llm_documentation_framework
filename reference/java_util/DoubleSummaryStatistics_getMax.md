#### getMax

```
public final double getMax()
```
Returns the maximum recorded value, `Double.NaN` if any recorded
value was NaN or `Double.NEGATIVE_INFINITY` if no values were
recorded. Unlike the numerical comparison operators, this method
considers negative zero to be strictly smaller than positive zero.
Returns:
the maximum recorded value, `Double.NaN` if any recorded
value was NaN or `Double.NEGATIVE_INFINITY` if no values were
recorded

