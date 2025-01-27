#### rangeClosed

```
static LongStream rangeClosed(long startInclusive,
                              long endInclusive)
```
Returns a sequential ordered `LongStream` from `startInclusive`
(inclusive) to `endInclusive` (inclusive) by an incremental step of
`1`.
API Note:
An equivalent sequence of increasing values can be produced
sequentially using a `for` loop as follows:
```

     for (long i = startInclusive; i <= endInclusive ; i++) { ... }
 
```

Parameters:
`startInclusive` - the (inclusive) initial value
`endInclusive` - the inclusive upper bound
Returns:
a sequential `LongStream` for the range of `long`
elements

