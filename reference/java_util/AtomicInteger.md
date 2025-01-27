```
public class AtomicInteger
extends Number
implements Serializable
```
An `int` value that may be updated atomically. See the
`java.util.concurrent.atomic` package specification for
description of the properties of atomic variables. An
`AtomicInteger` is used in applications such as atomically
incremented counters, and cannot be used as a replacement for an
`Integer`. However, this class does extend
`Number` to allow uniform access by tools and utilities that
deal with numerically-based classes.
Since:
1.5
See Also:
Serialized Form
