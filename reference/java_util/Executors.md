```
public class Executors
extends Object
```
Factory and utility methods for `Executor`, `ExecutorService`, `ScheduledExecutorService`, `ThreadFactory`, and `Callable` classes defined in this
package. This class supports the following kinds of methods:Methods that create and return an `ExecutorService`
set up with commonly useful configuration settings.Methods that create and return a `ScheduledExecutorService`
set up with commonly useful configuration settings.Methods that create and return a "wrapped" ExecutorService, that
disables reconfiguration by making implementation-specific methods
inaccessible.Methods that create and return a `ThreadFactory`
that sets newly created threads to a known state.Methods that create and return a `Callable`
out of other closure-like forms, so they can be used
in execution methods requiring `Callable`.
Since:
1.5
