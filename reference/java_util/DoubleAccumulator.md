```
public class DoubleAccumulator
extends Number
implements Serializable
```
One or more variables that together maintain a running `double`
value updated using a supplied function. When updates (method
`accumulate(double)`) are contended across threads, the set of variables
may grow dynamically to reduce contention. Method `get()`
(or, equivalently, `doubleValue()`) returns the current value
across the variables maintaining updates.This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.The supplied accumulator function should be side-effect-free,
since it may be re-applied when attempted updates fail due to
contention among threads. The function is applied with the current
value as its first argument, and the given update as the second
argument. For example, to maintain a running maximum value, you
could supply `Double::max` along with `Double.NEGATIVE_INFINITY` as the identity. The order of
accumulation within or across threads is not guaranteed. Thus, this
class may not be applicable if numerical stability is required,
especially when combining values of substantially different orders
of magnitude.Class `DoubleAdder` provides analogs of the functionality
of this class for the common special case of maintaining sums. The
call `new DoubleAdder()` is equivalent to `new
DoubleAccumulator((x, y) -> x + y, 0.0)`.This class extends `Number`, but does not define
methods such as `equals`, `hashCode` and `compareTo` because instances are expected to be mutated, and so are
not useful as collection keys.
Since:
1.8
See Also:
Serialized Form
