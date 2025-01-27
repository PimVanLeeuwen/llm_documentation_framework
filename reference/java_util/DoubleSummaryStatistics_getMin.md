#### getMin

```
public final double getMin()
```
Returns the minimum recorded value, `Double.NaN` if any recorded
value was NaN or `Double.POSITIVE_INFINITY` if no values were
recorded. Unlike the numerical comparison operators, this method
considers negative zero to be strictly smaller than positive zero.
Returns:
the minimum recorded value, `Double.NaN` if any recorded
value was NaN or `Double.POSITIVE_INFINITY` if no values were
recorded

