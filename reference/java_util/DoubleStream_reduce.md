#### reduce

```
OptionalDouble reduce(DoubleBinaryOperator op)
```
Performs a reduction on the
elements of this stream, using an
associative accumulation
function, and returns an `OptionalDouble` describing the reduced
value, if any. This is equivalent to:
```

     boolean foundAny = false;
     double result = null;
     for (double element : this stream) {
         if (!foundAny) {
             foundAny = true;
             result = element;
         }
         else
             result = accumulator.applyAsDouble(result, element);
     }
     return foundAny ? OptionalDouble.of(result) : OptionalDouble.empty();
 
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
`reduce(double, DoubleBinaryOperator)`

