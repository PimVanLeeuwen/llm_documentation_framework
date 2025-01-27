#### minBy

```
static <T> BinaryOperator<T> minBy(Comparator<? super T> comparator)
```
Returns a `BinaryOperator` which returns the lesser of two elements
according to the specified `Comparator`.
Type Parameters:
`T` - the type of the input arguments of the comparator
Parameters:
`comparator` - a `Comparator` for comparing the two values
Returns:
a `BinaryOperator` which returns the lesser of its operands,
according to the supplied `Comparator`
Throws:
`NullPointerException` - if the argument is null

