#### longs

```
public LongStream longs(long randomNumberOrigin,
                        long randomNumberBound)
```
Returns an effectively unlimited stream of pseudorandom `long` values, each conforming to the given origin (inclusive) and bound
(exclusive).A pseudorandom `long` value is generated as if it's the result
of calling the following method with the origin and bound:
```
 
 long nextLong(long origin, long bound) {
   long r = nextLong();
   long n = bound - origin, m = n - 1;
   if ((n & m) == 0L)  // power of two
     r = (r & m) + origin;
   else if (n > 0L) {  // reject over-represented candidates
     for (long u = r >>> 1;            // ensure nonnegative
          u + m - (r = u % n) < 0L;    // rejection check
          u = nextLong() >>> 1) // retry
         ;
     r += origin;
   }
   else {              // range not representable as long
     while (r < origin || r >= bound)
       r = nextLong();
   }
   return r;
 }
```

Implementation Note:
This method is implemented to be equivalent to `longs(Long.MAX_VALUE, randomNumberOrigin, randomNumberBound)`.
Parameters:
`randomNumberOrigin` - the origin (inclusive) of each random value
`randomNumberBound` - the bound (exclusive) of each random value
Returns:
a stream of pseudorandom `long` values,
each with the given origin (inclusive) and bound (exclusive)
Throws:
`IllegalArgumentException` - if `randomNumberOrigin`
is greater than or equal to `randomNumberBound`
Since:
1.8

