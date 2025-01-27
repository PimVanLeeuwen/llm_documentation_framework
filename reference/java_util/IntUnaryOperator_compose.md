#### compose

```
default IntUnaryOperator compose(IntUnaryOperator before)
```
Returns a composed operator that first applies the `before`
operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.
Parameters:
`before` - the operator to apply before this operator is applied
Returns:
a composed operator that first applies the `before`
operator and then applies this operator
Throws:
`NullPointerException` - if before is null
See Also:
`andThen(IntUnaryOperator)`

