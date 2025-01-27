```
public interface DoubleStream
extends BaseStream<Double,DoubleStream>
```
A sequence of primitive double-valued elements supporting sequential and parallel
aggregate operations. This is the `double` primitive specialization of
`Stream`.The following example illustrates an aggregate operation using
`Stream` and `DoubleStream`, computing the sum of the weights of the
red widgets:
```

     double sum = widgets.stream()
                         .filter(w -> w.getColor() == RED)
                         .mapToDouble(w -> w.getWeight())
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
