#### sum

```
int sum()
```
Returns the sum of elements in this stream. This is a special case
of a reduction
and is equivalent to:
```

     return reduce(0, Integer::sum);
 
```
This is a terminal
operation.
Returns:
the sum of elements in this stream

