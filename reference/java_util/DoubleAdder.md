```
public class DoubleAdder
extends Number
implements Serializable
```
One or more variables that together maintain an initially zero
`double` sum. When updates (method `add(double)`) are
contended across threads, the set of variables may grow dynamically
to reduce contention. Method `sum()` (or, equivalently `doubleValue()`) returns the current total combined across the
variables maintaining the sum. The order of accumulation within or
across threads is not guaranteed. Thus, this class may not be
applicable if numerical stability is required, especially when
combining values of substantially different orders of magnitude.This class is usually preferable to alternatives when multiple
threads update a common value that is used for purposes such as
summary statistics that are frequently updated but less frequently
read.This class extends `Number`, but does not define
methods such as `equals`, `hashCode` and `compareTo` because instances are expected to be mutated, and so are
not useful as collection keys.
Since:
1.8
See Also:
Serialized Form
