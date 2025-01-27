#### min

```
OptionalDouble min()
```
Returns an `OptionalDouble` describing the minimum element of this
stream, or an empty OptionalDouble if this stream is empty. The minimum
element will be `Double.NaN` if any stream element was NaN. Unlike
the numerical comparison operators, this method considers negative zero
to be strictly smaller than positive zero. This is a special case of a
reduction and is
equivalent to:
```

     return reduce(Double::min);
 
```
This is a terminal
operation.
Returns:
an `OptionalDouble` containing the minimum element of this
stream, or an empty optional if the stream is empty

