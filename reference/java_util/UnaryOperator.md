```
@FunctionalInterface
public interface UnaryOperator<T>
extends Function<T,T>
```
Represents an operation on a single operand that produces a result of the
same type as its operand. This is a specialization of `Function` for
the case where the operand and result are of the same type.This is a functional interface
whose functional method is `Function.apply(Object)`.
Since:
1.8
See Also:
`Function`
