#### sum

```
double sum()
```
Returns the sum of elements in this stream.
Summation is a special case of a reduction. If
floating-point summation were exact, this method would be
equivalent to:
```

     return reduce(0, Double::sum);
 
```
However, since floating-point summation is not exact, the above
code is not necessarily equivalent to the summation computation
done by this method.If any stream element is a NaN or the sum is at any point a NaN
then the sum will be NaN.
The value of a floating-point sum is a function both
of the input values as well as the order of addition
operations. The order of addition operations of this method is
intentionally not defined to allow for implementation
flexibility to improve the speed and accuracy of the computed
result.
In particular, this method may be implemented using compensated
summation or other technique to reduce the error bound in the
numerical sum compared to a simple summation of `double`
values.This is a terminal
operation.
API Note:
Elements sorted by increasing absolute magnitude tend
to yield more accurate results.
Returns:
the sum of elements in this stream

