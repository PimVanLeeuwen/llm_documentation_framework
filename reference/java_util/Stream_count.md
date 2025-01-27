#### count

```
long count()
```
Returns the count of elements in this stream. This is a special case of
a reduction and is
equivalent to:
```

     return mapToLong(e -> 1L).sum();
 
```
This is a terminal operation.
Returns:
the count of elements in this stream

