```
public class AtomicStampedReference<V>
extends Object
```
An `AtomicStampedReference` maintains an object reference
along with an integer "stamp", that can be updated atomically.Implementation note: This implementation maintains stamped
references by creating internal objects representing "boxed"
[reference, integer] pairs.
Since:
1.5
