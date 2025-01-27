```
public class LongSummaryStatistics
extends Object
implements LongConsumer, IntConsumer
```
A state object for collecting statistics such as count, min, max, sum, and
average.This class is designed to work with (though does not require)
streams. For example, you can compute
summary statistics on a stream of longs with:
```
 
 LongSummaryStatistics stats = longStream.collect(LongSummaryStatistics::new,
                                                  LongSummaryStatistics::accept,
                                                  LongSummaryStatistics::combine);
 
```
`LongSummaryStatistics` can be used as a
Stream.collect(Collector) reduction}
target for a stream. For example:
```
 
 LongSummaryStatistics stats = people.stream()
                                     .collect(Collectors.summarizingLong(Person::getAge));

```
This computes, in a single pass, the count of people, as well as the minimum,
maximum, sum, and average of their ages.
Implementation Note:
This implementation is not thread safe. However, it is safe to use
`Collectors.toLongStatistics()` on a parallel stream, because the parallel
implementation of `Stream.collect()`
provides the necessary partitioning, isolation, and merging of results for
safe and efficient parallel execution.This implementation does not check for overflow of the sum.
Since:
1.8
