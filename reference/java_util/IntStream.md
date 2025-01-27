```
public interface IntStream
extends BaseStream<Integer,IntStream>
```
A sequence of primitive int-valued elements supporting sequential and parallel
aggregate operations. This is the `int` primitive specialization of
`Stream`.The following example illustrates an aggregate operation using
`Stream` and `IntStream`, computing the sum of the weights of the
red widgets:
```

     int sum = widgets.stream()
                      .filter(w -> w.getColor() == RED)
                      .mapToInt(w -> w.getWeight())
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
