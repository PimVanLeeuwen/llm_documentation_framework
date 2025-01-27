```
public class AtomicMarkableReference<V>
extends Object
```
An `AtomicMarkableReference` maintains an object reference
along with a mark bit, that can be updated atomically.Implementation note: This implementation maintains markable
references by creating internal objects representing "boxed"
[reference, boolean] pairs.
Since:
1.5
