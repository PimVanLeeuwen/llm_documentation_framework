```
public abstract class AbstractQueuedLongSynchronizer
extends AbstractOwnableSynchronizer
implements Serializable
```
A version of `AbstractQueuedSynchronizer` in
which synchronization state is maintained as a `long`.
This class has exactly the same structure, properties, and methods
as `AbstractQueuedSynchronizer` with the exception
that all state-related parameters and results are defined
as `long` rather than `int`. This class
may be useful when creating synchronizers such as
multilevel locks and barriers that require
64 bits of state.See `AbstractQueuedSynchronizer` for usage
notes and examples.
Since:
1.6
See Also:
Serialized Form
