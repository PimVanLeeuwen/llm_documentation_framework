```
public class AtomicLong
extends Number
implements Serializable
```
A `long` value that may be updated atomically. See the
`java.util.concurrent.atomic` package specification for
description of the properties of atomic variables. An
`AtomicLong` is used in applications such as atomically
incremented sequence numbers, and cannot be used as a replacement
for a `Long`. However, this class does extend
`Number` to allow uniform access by tools and utilities that
deal with numerically-based classes.
Since:
1.5
See Also:
Serialized Form
