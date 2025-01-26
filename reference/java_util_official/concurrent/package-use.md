

Uses of Package java.util.concurrent (Java Platform SE 8 )




<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Uses of Package java.util.concurrent (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

PrevNextFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




Uses of Packagejava.util.concurrent

Packages that use java.util.concurrent PackageDescriptionjava.langProvides classes that are fundamental to the design of the Java
programming language.java.nio.channelsDefines channels, which represent connections to entities that are capable of
performing I/O operations, such as files and sockets; defines selectors, for
multiplexed, non-blocking I/O operations.java.nio.channels.spiService-provider classes for the `java.nio.channels` package.java.nio.fileDefines interfaces and classes for the Java virtual machine to access files,
file attributes, and file systems.java.nio.file.attributeInterfaces and classes providing access to file and file system attributes.java.nio.file.spiService-provider classes for the `java.nio.file` package.java.sqlProvides the API for accessing and processing data stored in a
data source (usually a relational database) using the
JavaTM programming language.java.util.concurrentUtility classes commonly useful in concurrent programming.java.util.concurrent.locksInterfaces and classes providing a framework for locking and waiting
for conditions that is distinct from built-in synchronization and
monitors.java.util.streamClasses to support functional-style operations on streams of elements, such
as map-reduce transformations on collections.javax.managementProvides the core classes for the Java Management Extensions.javax.swingProvides a set of "lightweight"
(all-Java language) components that,
to the maximum degree possible, work the same on all platforms.javax.toolsProvides interfaces for tools which can be invoked from a program,
for example, compilers.javax.xml.wsThis package contains the core JAX-WS APIs.javax.xml.ws.spiThis package defines SPIs for JAX-WS.

Classes in java.util.concurrent used by java.lang Class and DescriptionTimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by java.nio.channels Class and DescriptionExecutorService
An `Executor` that provides methods to manage termination and
methods that can produce a `Future` for tracking progress of
one or more asynchronous tasks.Future
A `Future` represents the result of an asynchronous
computation.ThreadFactory
An object that creates new threads on demand.TimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by java.nio.channels.spi Class and DescriptionExecutorService
An `Executor` that provides methods to manage termination and
methods that can produce a `Future` for tracking progress of
one or more asynchronous tasks.ThreadFactory
An object that creates new threads on demand.

Classes in java.util.concurrent used by java.nio.file Class and DescriptionTimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by java.nio.file.attribute Class and DescriptionTimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by java.nio.file.spi Class and DescriptionExecutorService
An `Executor` that provides methods to manage termination and
methods that can produce a `Future` for tracking progress of
one or more asynchronous tasks.

Classes in java.util.concurrent used by java.sql Class and DescriptionExecutor
An object that executes submitted `Runnable` tasks.

Classes in java.util.concurrent used by java.util.concurrent Class and DescriptionAbstractExecutorService
Provides default implementations of `ExecutorService`
execution methods.BlockingDeque
A `Deque` that additionally supports blocking operations that wait
for the deque to become non-empty when retrieving an element, and wait for
space to become available in the deque when storing an element.BlockingQueue
A `Queue` that additionally supports operations
that wait for the queue to become non-empty when retrieving an
element, and wait for space to become available in the queue when
storing an element.BrokenBarrierException
Exception thrown when a thread tries to wait upon a barrier that is
in a broken state, or which enters the broken state while the thread
is waiting.Callable
A task that returns a result and may throw an exception.CompletableFuture
A `Future` that may be explicitly completed (setting its
value and status), and may be used as a `CompletionStage`,
supporting dependent functions and actions that trigger upon its
completion.CompletionService
A service that decouples the production of new asynchronous tasks
from the consumption of the results of completed tasks.CompletionStage
A stage of a possibly asynchronous computation, that performs an
action or computes a value when another CompletionStage completes.ConcurrentHashMap.KeySetView
A view of a ConcurrentHashMap as a `Set` of keys, in
which additions may optionally be enabled by mapping to a
common value.ConcurrentMap
A `Map` providing thread safety and atomicity
guarantees.ConcurrentNavigableMap
A `ConcurrentMap` supporting `NavigableMap` operations,
and recursively so for its navigable sub-maps.ConcurrentSkipListMap
A scalable concurrent `ConcurrentNavigableMap` implementation.ConcurrentSkipListSet
A scalable concurrent `NavigableSet` implementation based on
a `ConcurrentSkipListMap`.CountedCompleter
A `ForkJoinTask` with a completion action performed when
triggered and there are no remaining pending actions.Delayed
A mix-in style interface for marking objects that should be
acted upon after a given delay.ExecutionException
Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception.Executor
An object that executes submitted `Runnable` tasks.ExecutorService
An `Executor` that provides methods to manage termination and
methods that can produce a `Future` for tracking progress of
one or more asynchronous tasks.ForkJoinPool
An `ExecutorService` for running `ForkJoinTask`s.ForkJoinPool.ForkJoinWorkerThreadFactory
Factory for creating new `ForkJoinWorkerThread`s.ForkJoinPool.ManagedBlocker
Interface for extending managed parallelism for tasks running
in `ForkJoinPool`s.ForkJoinTask
Abstract base class for tasks that run within a `ForkJoinPool`.ForkJoinWorkerThread
A thread managed by a `ForkJoinPool`, which executes
`ForkJoinTask`s.Future
A `Future` represents the result of an asynchronous
computation.Phaser
A reusable synchronization barrier, similar in functionality to
`CyclicBarrier` and
`CountDownLatch`
but supporting more flexible usage.RejectedExecutionHandler
A handler for tasks that cannot be executed by a `ThreadPoolExecutor`.RunnableFuture
A `Future` that is `Runnable`.RunnableScheduledFuture
A `ScheduledFuture` that is `Runnable`.ScheduledExecutorService
An `ExecutorService` that can schedule commands to run after a given
delay, or to execute periodically.ScheduledFuture
A delayed result-bearing action that can be cancelled.ThreadFactory
An object that creates new threads on demand.ThreadLocalRandom
A random number generator isolated to the current thread.ThreadPoolExecutor
An `ExecutorService` that executes each submitted task using
one of possibly several pooled threads, normally configured
using `Executors` factory methods.TimeoutException
Exception thrown when a blocking operation times out.TimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.TransferQueue
A `BlockingQueue` in which producers may wait for consumers
to receive elements.

Classes in java.util.concurrent used by java.util.concurrent.locks Class and DescriptionTimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by java.util.stream Class and DescriptionConcurrentMap
A `Map` providing thread safety and atomicity
guarantees.

Classes in java.util.concurrent used by javax.management Class and DescriptionExecutor
An object that executes submitted `Runnable` tasks.

Classes in java.util.concurrent used by javax.swing Class and DescriptionExecutionException
Exception thrown when attempting to retrieve the result of a task
that aborted by throwing an exception.Future
A `Future` represents the result of an asynchronous
computation.RunnableFuture
A `Future` that is `Runnable`.TimeoutException
Exception thrown when a blocking operation times out.TimeUnit
A `TimeUnit` represents time durations at a given unit of
granularity and provides utility methods to convert across units,
and to perform timing and delay operations in these units.

Classes in java.util.concurrent used by javax.tools Class and DescriptionCallable
A task that returns a result and may throw an exception.

Classes in java.util.concurrent used by javax.xml.ws Class and DescriptionExecutor
An object that executes submitted `Runnable` tasks.Future
A `Future` represents the result of an asynchronous
computation.

Classes in java.util.concurrent used by javax.xml.ws.spi Class and DescriptionExecutor
An object that executes submitted `Runnable` tasks.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

PrevNextFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_bottom");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->



 Submit a bug or feature For further API reference and developer documentation, see Java SE Documentation. That documentation contains more detailed, developer-targeted descriptions, with conceptual overviews, definitions of terms, workarounds, and working code examples. Copyright © 1993, 2025, Oracle and/or its affiliates. All rights reserved. Use is subject to license terms. Also see the documentation redistribution policy. 

