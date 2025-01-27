#### max

```
OptionalInt max()
```
Returns an `OptionalInt` describing the maximum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a reduction
and is equivalent to:
```

     return reduce(Integer::max);
 
```
This is a terminal
operation.
Returns:
an `OptionalInt` containing the maximum element of this
stream, or an empty `OptionalInt` if the stream is empty

