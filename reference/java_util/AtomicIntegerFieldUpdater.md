```
public abstract class AtomicIntegerFieldUpdater<T>
extends Object
```
A reflection-based utility that enables atomic updates to
designated `volatile int` fields of designated classes.
This class is designed for use in atomic data structures in which
several fields of the same node are independently subject to atomic
updates.Note that the guarantees of the `compareAndSet`
method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of
`compareAndSet` and `set` on the same updater.
Since:
1.5
