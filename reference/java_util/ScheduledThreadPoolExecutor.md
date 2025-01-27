```
public class ScheduledThreadPoolExecutor
extends ThreadPoolExecutor
implements ScheduledExecutorService
```
A `ThreadPoolExecutor` that can additionally schedule
commands to run after a given delay, or to execute
periodically. This class is preferable to `Timer`
when multiple worker threads are needed, or when the additional
flexibility or capabilities of `ThreadPoolExecutor` (which
this class extends) are required.Delayed tasks execute no sooner than they are enabled, but
without any real-time guarantees about when, after they are
enabled, they will commence. Tasks scheduled for exactly the same
execution time are enabled in first-in-first-out (FIFO) order of
submission.When a submitted task is cancelled before it is run, execution
is suppressed. By default, such a cancelled task is not
automatically removed from the work queue until its delay
elapses. While this enables further inspection and monitoring, it
may also cause unbounded retention of cancelled tasks. To avoid
this, set `setRemoveOnCancelPolicy(boolean)` to `true`, which
causes tasks to be immediately removed from the work queue at
time of cancellation.Successive executions of a task scheduled via
`scheduleAtFixedRate` or
`scheduleWithFixedDelay` do not overlap. While different
executions may be performed by different threads, the effects of
prior executions happen-before
those of subsequent ones.While this class inherits from `ThreadPoolExecutor`, a few
of the inherited tuning methods are not useful for it. In
particular, because it acts as a fixed-sized pool using
`corePoolSize` threads and an unbounded queue, adjustments
to `maximumPoolSize` have no useful effect. Additionally, it
is almost never a good idea to set `corePoolSize` to zero or
use `allowCoreThreadTimeOut` because this may leave the pool
without threads to handle tasks once they become eligible to run.Extension notes: This class overrides the
`execute` and
`submit`
methods to generate internal `ScheduledFuture` objects to
control per-task delays and scheduling. To preserve
functionality, any further overrides of these methods in
subclasses must invoke superclass versions, which effectively
disables additional task customization. However, this class
provides alternative protected extension method
`decorateTask` (one version each for `Runnable` and
`Callable`) that can be used to customize the concrete task
types used to execute commands entered via `execute`,
`submit`, `schedule`, `scheduleAtFixedRate`,
and `scheduleWithFixedDelay`. By default, a
`ScheduledThreadPoolExecutor` uses a task type extending
`FutureTask`. However, this may be modified or replaced using
subclasses of the form:
```
 
 public class CustomScheduledExecutor extends ScheduledThreadPoolExecutor {

   static class CustomTask<V> implements RunnableScheduledFuture<V> { ... }

   protected <V> RunnableScheduledFuture<V> decorateTask(
                Runnable r, RunnableScheduledFuture<V> task) {
       return new CustomTask<V>(r, task);
   }

   protected <V> RunnableScheduledFuture<V> decorateTask(
                Callable<V> c, RunnableScheduledFuture<V> task) {
       return new CustomTask<V>(c, task);
   }
   // ... add constructors, etc.
 }
```

Since:
1.5
