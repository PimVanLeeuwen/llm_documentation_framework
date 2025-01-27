#### reduce

```
OptionalLong reduce(LongBinaryOperator op)
```
Performs a reduction on the
elements of this stream, using an
associative accumulation
function, and returns an `OptionalLong` describing the reduced value,
if any. This is equivalent to:
```

     boolean foundAny = false;
     long result = null;
     for (long element : this stream) {
         if (!foundAny) {
             foundAny = true;
             result = element;
         }
         else
             result = accumulator.applyAsLong(result, element);
     }
     return foundAny ? OptionalLong.of(result) : OptionalLong.empty();
 
```
but is not constrained to execute sequentially.The `accumulator` function must be an
associative function.This is a terminal
operation.
Parameters:
`op` - an associative,
non-interfering,
stateless
function for combining two values
Returns:
the result of the reduction
See Also:
`reduce(long, LongBinaryOperator)`

