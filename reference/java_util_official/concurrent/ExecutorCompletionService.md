

ExecutorCompletionService (Java Platform SE 8 )








<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ExecutorCompletionService (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method




compact1, compact2, compact3
java.util.concurrentClass ExecutorCompletionService<V>
java.lang.Objectjava.util.concurrent.ExecutorCompletionService<V>
All Implemented Interfaces:
CompletionService<V>


```
public class ExecutorCompletionService<V>
extends Object
implements CompletionService<V>
```
A `CompletionService` that uses a supplied `Executor`
to execute tasks. This class arranges that submitted tasks are,
upon completion, placed on a queue accessible using `take`.
The class is lightweight enough to be suitable for transient use
when processing groups of tasks.Usage Examples.
Suppose you have a set of solvers for a certain problem, each
returning a value of some type `Result`, and would like to
run them concurrently, processing the results of each of them that
return a non-null value, in some method `use(Result r)`. You
could write this as:
```
 
 void solve(Executor e,
            Collection<Callable<Result>> solvers)
     throws InterruptedException, ExecutionException {
     CompletionService<Result> ecs
         = new ExecutorCompletionService<Result>(e);
     for (Callable<Result> s : solvers)
         ecs.submit(s);
     int n = solvers.size();
     for (int i = 0; i < n; ++i) {
         Result r = ecs.take().get();
         if (r != null)
             use(r);
     }
 }
```
Suppose instead that you would like to use the first non-null result
of the set of tasks, ignoring any that encounter exceptions,
and cancelling all other tasks when the first one is ready:
```
 
 void solve(Executor e,
            Collection<Callable<Result>> solvers)
     throws InterruptedException {
     CompletionService<Result> ecs
         = new ExecutorCompletionService<Result>(e);
     int n = solvers.size();
     List<Future<Result>> futures
         = new ArrayList<Future<Result>>(n);
     Result result = null;
     try {
         for (Callable<Result> s : solvers)
             futures.add(ecs.submit(s));
         for (int i = 0; i < n; ++i) {
             try {
                 Result r = ecs.take().get();
                 if (r != null) {
                     result = r;
                     break;
                 }
             } catch (ExecutionException ignore) {}
         }
     }
     finally {
         for (Future<Result> f : futures)
             f.cancel(true);
     }

     if (result != null)
         use(result);
 }
```

### Constructor Summary

Constructors Constructor and Description`ExecutorCompletionService(Executor executor)`
Creates an ExecutorCompletionService using the supplied
executor for base task execution and a
`LinkedBlockingQueue` as a completion queue.`ExecutorCompletionService(Executor executor,
BlockingQueue<Future<V>> completionQueue)`
Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`Future<V>``poll()`
Retrieves and removes the Future representing the next
completed task, or `null` if none are present.`Future<V>``poll(long timeout,
TimeUnit unit)`
Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.`Future<V>``submit(Callable<V> task)`
Submits a value-returning task for execution and returns a Future
representing the pending results of the task.`Future<V>``submit(Runnable task,
V result)`
Submits a Runnable task for execution and returns a Future
representing that task.`Future<V>``take()`
Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### ExecutorCompletionService

```
public ExecutorCompletionService(Executor executor)
```
Creates an ExecutorCompletionService using the supplied
executor for base task execution and a
`LinkedBlockingQueue` as a completion queue.
Parameters:
`executor` - the executor to use
Throws:
`NullPointerException` - if executor is `null`

#### ExecutorCompletionService

```
public ExecutorCompletionService(Executor executor,
                                 BlockingQueue<Future<V>> completionQueue)
```
Creates an ExecutorCompletionService using the supplied
executor for base task execution and the supplied queue as its
completion queue.
Parameters:
`executor` - the executor to use
`completionQueue` - the queue to use as the completion queue
normally one dedicated for use by this service. This
queue is treated as unbounded -- failed attempted
`Queue.add` operations for completed tasks cause
them not to be retrievable.
Throws:
`NullPointerException` - if executor or completionQueue are `null`

### Method Detail

#### submit

```
public Future<V> submit(Callable<V> task)
```
Description copied from interface: `CompletionService`
Submits a value-returning task for execution and returns a Future
representing the pending results of the task. Upon completion,
this task may be taken or polled.
Specified by:
`submit` in interface `CompletionService<V>`
Parameters:
`task` - the task to submit
Returns:
a Future representing pending completion of the task

#### submit

```
public Future<V> submit(Runnable task,
                        V result)
```
Description copied from interface: `CompletionService`
Submits a Runnable task for execution and returns a Future
representing that task. Upon completion, this task may be
taken or polled.
Specified by:
`submit` in interface `CompletionService<V>`
Parameters:
`task` - the task to submit
`result` - the result to return upon successful completion
Returns:
a Future representing pending completion of the task,
and whose `get()` method will return the given
result value upon completion

#### take

```
public Future<V> take()
               throws InterruptedException
```
Description copied from interface: `CompletionService`
Retrieves and removes the Future representing the next
completed task, waiting if none are yet present.
Specified by:
`take` in interface `CompletionService<V>`
Returns:
the Future representing the next completed task
Throws:
`InterruptedException` - if interrupted while waiting

#### poll

```
public Future<V> poll()
```
Description copied from interface: `CompletionService`
Retrieves and removes the Future representing the next
completed task, or `null` if none are present.
Specified by:
`poll` in interface `CompletionService<V>`
Returns:
the Future representing the next completed task, or
`null` if none are present

#### poll

```
public Future<V> poll(long timeout,
                      TimeUnit unit)
               throws InterruptedException
```
Description copied from interface: `CompletionService`
Retrieves and removes the Future representing the next
completed task, waiting if necessary up to the specified wait
time if none are yet present.
Specified by:
`poll` in interface `CompletionService<V>`
Parameters:
`timeout` - how long to wait before giving up, in units of
`unit`
`unit` - a `TimeUnit` determining how to interpret the
`timeout` parameter
Returns:
the Future representing the next completed task or
`null` if the specified waiting time elapses
before one is present
Throws:
`InterruptedException` - if interrupted while waiting




Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev ClassNext ClassFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->


Summary:Nested |Field |Constr |MethodDetail:Field |Constr |Method


 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

