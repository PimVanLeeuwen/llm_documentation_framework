```
public interface BaseStream<T,S extends BaseStream<T,S>>
extends AutoCloseable
```
Base interface for streams, which are sequences of elements supporting
sequential and parallel aggregate operations. The following example
illustrates an aggregate operation using the stream types `Stream`
and `IntStream`, computing the sum of the weights of the red widgets:
```

     int sum = widgets.stream()
                      .filter(w -> w.getColor() == RED)
                      .mapToInt(w -> w.getWeight())
                      .sum();
 
```
See the class documentation for `Stream` and the package documentation
for java.util.stream for additional
specification of streams, stream operations, stream pipelines, and
parallelism, which governs the behavior of all stream types.
Since:
1.8
See Also:
`Stream`,
`IntStream`,
`LongStream`,
`DoubleStream`,
java.util.stream
