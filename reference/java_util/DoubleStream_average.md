#### average

```
OptionalDouble average()
```
Returns an `OptionalDouble` describing the arithmetic
mean of elements of this stream, or an empty optional if this
stream is empty.
If any recorded value is a NaN or the sum is at any point a NaN
then the average will be NaN.The average returned can vary depending upon the order in
which values are recorded.
This method may be implemented using compensated summation or
other technique to reduce the error bound in the `numerical sum` used to compute the average.The average is a special case of a reduction.This is a terminal
operation.
API Note:
Elements sorted by increasing absolute magnitude tend
to yield more accurate results.
Returns:
an `OptionalDouble` containing the average element of this
stream, or an empty optional if the stream is empty

