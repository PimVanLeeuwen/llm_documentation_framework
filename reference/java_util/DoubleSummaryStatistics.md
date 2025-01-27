```
public class DoubleSummaryStatistics
extends Object
implements DoubleConsumer
```
A state object for collecting statistics such as count, min, max, sum, and
average.This class is designed to work with (though does not require)
streams. For example, you can compute
summary statistics on a stream of doubles with:
```
 
 DoubleSummaryStatistics stats = doubleStream.collect(DoubleSummaryStatistics::new,
                                                      DoubleSummaryStatistics::accept,
                                                      DoubleSummaryStatistics::combine);
 
```
`DoubleSummaryStatistics` can be used as a
reduction
target for a stream. For example:
```
 
 DoubleSummaryStatistics stats = people.stream()
     .collect(Collectors.summarizingDouble(Person::getWeight));

```
This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their weights.
Implementation Note:
This implementation is not thread safe. However, it is safe to use
`Collectors.toDoubleStatistics()` on a parallel stream, because the parallel
implementation of `Stream.collect()`
provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.
Since:
1.8
