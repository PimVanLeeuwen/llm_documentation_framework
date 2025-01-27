#### managedBlock

```
public static void managedBlock(ForkJoinPool.ManagedBlocker blocker)
                         throws InterruptedException
```
Runs the given possibly blocking task. When running in a ForkJoinPool, this
method possibly arranges for a spare thread to be activated if
necessary to ensure sufficient parallelism while the current
thread is blocked in `blocker.block()`.This method repeatedly calls `blocker.isReleasable()` and
`blocker.block()` until either method returns `true`.
Every call to `blocker.block()` is preceded by a call to
`blocker.isReleasable()` that returned `false`.If not running in a ForkJoinPool, this method is
behaviorally equivalent to
```
 
 while (!blocker.isReleasable())
   if (blocker.block())
     break;
```
If running in a ForkJoinPool, the pool may first be expanded to
ensure sufficient parallelism available during the call to
`blocker.block()`.
Parameters:
`blocker` - the blocker task
Throws:
`InterruptedException` - if `blocker.block()` did so

