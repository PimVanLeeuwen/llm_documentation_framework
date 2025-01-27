#### rangeClosed

```
static IntStream rangeClosed(int startInclusive,
                             int endInclusive)
```
Returns a sequential ordered `IntStream` from `startInclusive`
(inclusive) to `endInclusive` (inclusive) by an incremental step of
`1`.
API Note:
An equivalent sequence of increasing values can be produced
sequentially using a `for` loop as follows:
```

     for (int i = startInclusive; i <= endInclusive ; i++) { ... }
 
```

Parameters:
`startInclusive` - the (inclusive) initial value
`endInclusive` - the inclusive upper bound
Returns:
a sequential `IntStream` for the range of `int`
elements

