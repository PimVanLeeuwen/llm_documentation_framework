#### reduce

```
OptionalInt reduce(IntBinaryOperator op)
```
Performs a reduction on the
elements of this stream, using an
associative accumulation
function, and returns an `OptionalInt` describing the reduced value,
if any. This is equivalent to:
```

     boolean foundAny = false;
     int result = null;
     for (int element : this stream) {
         if (!foundAny) {
             foundAny = true;
             result = element;
         }
         else
             result = accumulator.applyAsInt(result, element);
     }
     return foundAny ? OptionalInt.of(result) : OptionalInt.empty();
 
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
`reduce(int, IntBinaryOperator)`

