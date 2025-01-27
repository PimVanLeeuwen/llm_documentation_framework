```
@FunctionalInterface
public interface BinaryOperator<T>
extends BiFunction<T,T,T>
```
Represents an operation upon two operands of the same type, producing a result
of the same type as the operands. This is a specialization of
`BiFunction` for the case where the operands and the result are all of
the same type.This is a functional interface
whose functional method is `BiFunction.apply(Object, Object)`.
Since:
1.8
See Also:
`BiFunction`,
`UnaryOperator`
