#### reset

```
public void reset()
```
Resets the barrier to its initial state. If any parties are
currently waiting at the barrier, they will return with a
`BrokenBarrierException`. Note that resets after
a breakage has occurred for other reasons can be complicated to
carry out; threads need to re-synchronize in some other way,
and choose one to perform the reset. It may be preferable to
instead create a new barrier for subsequent use.

