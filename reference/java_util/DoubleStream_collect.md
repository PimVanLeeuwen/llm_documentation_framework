#### collect

```
<R> R collect(Supplier<R> supplier,
              ObjDoubleConsumer<R> accumulator,
              BiConsumer<R,R> combiner)
```
Performs a mutable
reduction operation on the elements of this stream. A mutable
reduction is one in which the reduced value is a mutable result container,
such as an `ArrayList`, and elements are incorporated by updating
the state of the result rather than by replacing the result. This
produces a result equivalent to:
```

     R result = supplier.get();
     for (double element : this stream)
         accumulator.accept(result, element);
     return result;
 
```
Like `reduce(double, DoubleBinaryOperator)`, `collect`
operations can be parallelized without requiring additional
synchronization.This is a terminal
operation.
Type Parameters:
`R` - type of the result
Parameters:
`supplier` - a function that creates a new result container. For a
parallel execution, this function may be called
multiple times and must return a fresh value each time.
`accumulator` - an associative,
non-interfering,
stateless
function for incorporating an additional element into a result
`combiner` - an associative,
non-interfering,
stateless
function for combining two values, which must be
compatible with the accumulator function
Returns:
the result of the reduction
See Also:
`Stream.collect(Supplier, BiConsumer, BiConsumer)`

