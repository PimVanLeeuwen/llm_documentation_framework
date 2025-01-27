#### privilegedThreadFactory

```
public static ThreadFactory privilegedThreadFactory()
```
Returns a thread factory used to create new threads that
have the same permissions as the current thread.
This factory creates threads with the same settings as `defaultThreadFactory()`, additionally setting the
AccessControlContext and contextClassLoader of new threads to
be the same as the thread invoking this
`privilegedThreadFactory` method. A new
`privilegedThreadFactory` can be created within an
`AccessController.doPrivileged`
action setting the current thread's access control context to
create threads with the selected permission settings holding
within that action.Note that while tasks running within such threads will have
the same access control and class loader settings as the
current thread, they need not have the same `ThreadLocal` or `InheritableThreadLocal` values. If necessary,
particular values of thread locals can be set or reset before
any task runs in `ThreadPoolExecutor` subclasses using
`ThreadPoolExecutor.beforeExecute(Thread, Runnable)`.
Also, if it is necessary to initialize worker threads to have
the same InheritableThreadLocal settings as some other
designated thread, you can create a custom ThreadFactory in
which that thread waits for and services requests to create
others that will inherit its values.
Returns:
a thread factory
Throws:
`AccessControlException` - if the current access control
context does not have permission to both get and set context
class loader

