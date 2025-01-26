

AbstractQueuedSynchronizer.ConditionObject (Java Platform SE 8 )














<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="AbstractQueuedSynchronizer.ConditionObject (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10,"i9":10};
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
java.util.concurrent.locksClass AbstractQueuedSynchronizer.ConditionObject
java.lang.Objectjava.util.concurrent.locks.AbstractQueuedSynchronizer.ConditionObject
All Implemented Interfaces:
Serializable, Condition

Enclosing class:
AbstractQueuedSynchronizer


```
public class AbstractQueuedSynchronizer.ConditionObject
extends Object
implements Condition, Serializable
```
Condition implementation for a `AbstractQueuedSynchronizer` serving as the basis of a `Lock` implementation.Method documentation for this class describes mechanics,
not behavioral specifications from the point of view of Lock
and Condition users. Exported versions of this class will in
general need to be accompanied by documentation describing
condition semantics that rely on those of the associated
`AbstractQueuedSynchronizer`.This class is Serializable, but all fields are transient,
so deserialized conditions have no waiters.
See Also:
Serialized Form

### Constructor Summary

Constructors Constructor and Description`ConditionObject()`
Creates a new `ConditionObject` instance.

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`void``await()`
Implements interruptible condition wait.`boolean``await(long time,
TimeUnit unit)`
Implements timed condition wait.`long``awaitNanos(long nanosTimeout)`
Implements timed condition wait.`void``awaitUninterruptibly()`
Implements uninterruptible condition wait.`boolean``awaitUntil(Date deadline)`
Implements absolute timed condition wait.`protected Collection<Thread>``getWaitingThreads()`
Returns a collection containing those threads that may be
waiting on this Condition.`protected int``getWaitQueueLength()`
Returns an estimate of the number of threads waiting on
this condition.`protected boolean``hasWaiters()`
Queries whether any threads are waiting on this condition.`void``signal()`
Moves the longest-waiting thread, if one exists, from the
wait queue for this condition to the wait queue for the
owning lock.`void``signalAll()`
Moves all threads from the wait queue for this condition to
the wait queue for the owning lock.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Constructor Detail

#### ConditionObject

```
public ConditionObject()
```
Creates a new `ConditionObject` instance.

### Method Detail

#### signal

```
public final void signal()
```
Moves the longest-waiting thread, if one exists, from the
wait queue for this condition to the wait queue for the
owning lock.
Specified by:
`signal` in interface `Condition`
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

#### signalAll

```
public final void signalAll()
```
Moves all threads from the wait queue for this condition to
the wait queue for the owning lock.
Specified by:
`signalAll` in interface `Condition`
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

#### awaitUninterruptibly

```
public final void awaitUninterruptibly()
```
Implements uninterruptible condition wait.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.
Specified by:
`awaitUninterruptibly` in interface `Condition`

#### await

```
public final void await()
                 throws InterruptedException
```
Implements interruptible condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled or interrupted.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.
Specified by:
`await` in interface `Condition`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

#### awaitNanos

```
public final long awaitNanos(long nanosTimeout)
                      throws InterruptedException
```
Implements timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.
Specified by:
`awaitNanos` in interface `Condition`
Parameters:
`nanosTimeout` - the maximum time to wait, in nanoseconds
Returns:
an estimate of the `nanosTimeout` value minus
the time spent waiting upon return from this method.
A positive value may be used as the argument to a
subsequent call to this method to finish waiting out
the desired time. A value less than or equal to zero
indicates that no time remains.
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

#### awaitUntil

```
public final boolean awaitUntil(Date deadline)
                         throws InterruptedException
```
Implements absolute timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.If timed out while blocked in step 4, return false, else true.
Specified by:
`awaitUntil` in interface `Condition`
Parameters:
`deadline` - the absolute time to wait until
Returns:
`false` if the deadline has elapsed upon return, else
`true`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

#### await

```
public final boolean await(long time,
                           TimeUnit unit)
                    throws InterruptedException
```
Implements timed condition wait.If current thread is interrupted, throw InterruptedException.Save lock state returned by `AbstractQueuedSynchronizer.getState()`.Invoke `AbstractQueuedSynchronizer.release(int)` with saved state as argument,
throwing IllegalMonitorStateException if it fails.Block until signalled, interrupted, or timed out.Reacquire by invoking specialized version of
`AbstractQueuedSynchronizer.acquire(int)` with saved state as argument.If interrupted while blocked in step 4, throw InterruptedException.If timed out while blocked in step 4, return false, else true.
Specified by:
`await` in interface `Condition`
Parameters:
`time` - the maximum time to wait
`unit` - the time unit of the `time` argument
Returns:
`false` if the waiting time detectably elapsed
before return from the method, else `true`
Throws:
`InterruptedException` - if the current thread is interrupted
(and interruption of thread suspension is supported)

#### hasWaiters

```
protected final boolean hasWaiters()
```
Queries whether any threads are waiting on this condition.
Implements `AbstractQueuedSynchronizer.hasWaiters(ConditionObject)`.
Returns:
`true` if there are any waiting threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

#### getWaitQueueLength

```
protected final int getWaitQueueLength()
```
Returns an estimate of the number of threads waiting on
this condition.
Implements `AbstractQueuedSynchronizer.getWaitQueueLength(ConditionObject)`.
Returns:
the estimated number of waiting threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`

#### getWaitingThreads

```
protected final Collection<Thread> getWaitingThreads()
```
Returns a collection containing those threads that may be
waiting on this Condition.
Implements `AbstractQueuedSynchronizer.getWaitingThreads(ConditionObject)`.
Returns:
the collection of threads
Throws:
`IllegalMonitorStateException` - if `AbstractQueuedSynchronizer.isHeldExclusively()`
returns `false`




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

