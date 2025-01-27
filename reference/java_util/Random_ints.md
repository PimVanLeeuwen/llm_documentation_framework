#### ints

```
public IntStream ints(int randomNumberOrigin,
                      int randomNumberBound)
```
Returns an effectively unlimited stream of pseudorandom `int` values, each conforming to the given origin (inclusive) and bound
(exclusive).A pseudorandom `int` value is generated as if it's the result of
calling the following method with the origin and bound:
```
 
 int nextInt(int origin, int bound) {
   int n = bound - origin;
   if (n > 0) {
     return nextInt(n) + origin;
   }
   else {  // range not representable as int
     int r;
     do {
       r = nextInt();
     } while (r < origin || r >= bound);
     return r;
   }
 }
```

Implementation Note:
This method is implemented to be equivalent to `ints(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)`.
Parameters:
`randomNumberOrigin` - the origin (inclusive) of each random value
`randomNumberBound` - the bound (exclusive) of each random value
Returns:
a stream of pseudorandom `int` values,
each with the given origin (inclusive) and bound (exclusive)
Throws:
`IllegalArgumentException` - if `randomNumberOrigin`
is greater than or equal to `randomNumberBound`
Since:
1.8

