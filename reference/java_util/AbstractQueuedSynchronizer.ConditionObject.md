```
public class AbstractQueuedSynchronizer.ConditionObject
extends Object
implements Condition, Serializable
```
Condition implementation for a `AbstractQueuedSynchronizer` serving as the basis of a `Lock` implementation.Method documentation for this class describes mechanics,
not behavioral specifications from the point of view of Lock
and Condition users. Exported versions of this class will in
general need to be accompanied by documentation describing
condition semantics that rely on those of the associated
`AbstractQueuedSynchronizer`.This class is Serializable, but all fields are transient,
so deserialized conditions have no waiters.
See Also:
Serialized Form
