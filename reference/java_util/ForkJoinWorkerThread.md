```
public class ForkJoinWorkerThread
extends Thread
```
A thread managed by a `ForkJoinPool`, which executes
`ForkJoinTask`s.
This class is subclassable solely for the sake of adding
functionality -- there are no overridable methods dealing with
scheduling or execution. However, you can override initialization
and termination methods surrounding the main task processing loop.
If you do create such a subclass, you will also need to supply a
custom `ForkJoinPool.ForkJoinWorkerThreadFactory` to
use it in a `ForkJoinPool`.
Since:
1.7
