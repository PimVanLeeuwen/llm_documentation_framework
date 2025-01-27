#### min

```
OptionalLong min()
```
Returns an `OptionalLong` describing the minimum element of this
stream, or an empty optional if this stream is empty. This is a special
case of a reduction
and is equivalent to:
```

     return reduce(Long::min);
 
```
This is a terminal operation.
Returns:
an `OptionalLong` containing the minimum element of this
stream, or an empty `OptionalLong` if the stream is empty

