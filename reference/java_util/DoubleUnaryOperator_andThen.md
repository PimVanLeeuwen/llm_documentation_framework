#### andThen

```
default DoubleUnaryOperator andThen(DoubleUnaryOperator after)
```
Returns a composed operator that first applies this operator to
its input, and then applies the `after` operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.
Parameters:
`after` - the operator to apply after this operator is applied
Returns:
a composed operator that first applies this operator and then
applies the `after` operator
Throws:
`NullPointerException` - if after is null
See Also:
`compose(DoubleUnaryOperator)`

