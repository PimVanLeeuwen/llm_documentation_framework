```
public interface LongStream
extends BaseStream<Long,LongStream>
```
A sequence of primitive long-valued elements supporting sequential and parallel
aggregate operations. This is the `long` primitive specialization of
`Stream`.The following example illustrates an aggregate operation using
`Stream` and `LongStream`, computing the sum of the weights of the
red widgets:
```

     long sum = widgets.stream()
                       .filter(w -> w.getColor() == RED)
                       .mapToLong(w -> w.getWeight())
                       .sum();
 
```
See the class documentation for `Stream` and the package documentation
for java.util.stream for additional
specification of streams, stream operations, stream pipelines, and
parallelism.
Since:
1.8
See Also:
`Stream`,
java.util.stream
