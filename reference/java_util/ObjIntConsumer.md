```
@FunctionalInterface
public interface ObjIntConsumer<T>
```
Represents an operation that accepts an object-valued and a
`int`-valued argument, and returns no result. This is the
`(reference, int)` specialization of `BiConsumer`.
Unlike most other functional interfaces, `ObjIntConsumer` is
expected to operate via side-effects.This is a functional interface
whose functional method is `accept(Object, int)`.
Since:
1.8
See Also:
`BiConsumer`
