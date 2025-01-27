```
public interface Delayed
extends Comparable<Delayed>
```
A mix-in style interface for marking objects that should be
acted upon after a given delay.An implementation of this interface must define a
`compareTo` method that provides an ordering consistent with
its `getDelay` method.
Since:
1.5
