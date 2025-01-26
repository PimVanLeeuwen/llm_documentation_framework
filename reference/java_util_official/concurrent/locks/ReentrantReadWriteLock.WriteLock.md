

ReentrantReadWriteLock.WriteLock (Java Platform SE 8 )













<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ReentrantReadWriteLock.WriteLock (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":10,"i1":10,"i2":10,"i3":10,"i4":10,"i5":10,"i6":10,"i7":10,"i8":10};
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
java.util.concurrent.locksClass ReentrantReadWriteLock.WriteLock
java.lang.Objectjava.util.concurrent.locks.ReentrantReadWriteLock.WriteLock
All Implemented Interfaces:
Serializable, Lock

Enclosing class:
ReentrantReadWriteLock


```
public static class ReentrantReadWriteLock.WriteLock
extends Object
implements Lock, Serializable
```
The lock returned by method `ReentrantReadWriteLock.writeLock()`.
See Also:
Serialized Form

### Constructor Summary

Constructors ModifierConstructor and Description`protected` `WriteLock(ReentrantReadWriteLock lock)`
Constructor for use by subclasses

### Method Summary

All Methods Instance Methods Concrete Methods Modifier and TypeMethod and Description`int``getHoldCount()`
Queries the number of holds on this write lock by the current
thread.`boolean``isHeldByCurrentThread()`
Queries if this write lock is held by the current thread.`void``lock()`
Acquires the write lock.`void``lockInterruptibly()`
Acquires the write lock unless the current thread is
interrupted.`Condition``newCondition()`
Returns a `Condition` instance for use with this
`Lock` instance.`String``toString()`
Returns a string identifying this lock, as well as its lock
state.`boolean``tryLock()`
Acquires the write lock only if it is not held by another thread
at the time of invocation.`boolean``tryLock(long timeout,
TimeUnit unit)`
Acquires the write lock if it is not held by another thread
within the given waiting time and the current thread has
not been interrupted.`void``unlock()`
Attempts to release this lock.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Constructor Detail

#### WriteLock

```
protected WriteLock(ReentrantReadWriteLock lock)
```
Constructor for use by subclasses
Parameters:
`lock` - the outer lock object
Throws:
`NullPointerException` - if the lock is null

### Method Detail

#### lock

```
public void lock()
```
Acquires the write lock.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately, setting the write lock hold count to
one.If the current thread already holds the write lock then the
hold count is incremented by one and the method returns
immediately.If the lock is held by another thread then the current
thread becomes disabled for thread scheduling purposes and
lies dormant until the write lock has been acquired, at which
time the write lock hold count is set to one.
Specified by:
`lock` in interface `Lock`

#### lockInterruptibly

```
public void lockInterruptibly()
                       throws InterruptedException
```
Acquires the write lock unless the current thread is
interrupted.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately, setting the write lock hold count to
one.If the current thread already holds this lock then the
hold count is incremented by one and the method returns
immediately.If the lock is held by another thread then the current
thread becomes disabled for thread scheduling purposes and
lies dormant until one of two things happens:The write lock is acquired by the current thread; orSome other thread interrupts
the current thread.If the write lock is acquired by the current thread then the
lock hold count is set to one.If the current thread:has its interrupted status set on entry to this method;
oris interrupted while
acquiring the write lock,then `InterruptedException` is thrown and the current
thread's interrupted status is cleared.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock.
Specified by:
`lockInterruptibly` in interface `Lock`
Throws:
`InterruptedException` - if the current thread is interrupted

#### tryLock

```
public boolean tryLock()
```
Acquires the write lock only if it is not held by another thread
at the time of invocation.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately with the value `true`,
setting the write lock hold count to one. Even when this lock has
been set to use a fair ordering policy, a call to
`tryLock()` will immediately acquire the
lock if it is available, whether or not other threads are
currently waiting for the write lock. This "barging"
behavior can be useful in certain circumstances, even
though it breaks fairness. If you want to honor the
fairness setting for this lock, then use `tryLock(0, TimeUnit.SECONDS)` 
which is almost equivalent (it also detects interruption).If the current thread already holds this lock then the
hold count is incremented by one and the method returns
`true`.If the lock is held by another thread then this method
will return immediately with the value `false`.
Specified by:
`tryLock` in interface `Lock`
Returns:
`true` if the lock was free and was acquired
by the current thread, or the write lock was already held
by the current thread; and `false` otherwise.

#### tryLock

```
public boolean tryLock(long timeout,
                       TimeUnit unit)
                throws InterruptedException
```
Acquires the write lock if it is not held by another thread
within the given waiting time and the current thread has
not been interrupted.Acquires the write lock if neither the read nor write lock
are held by another thread
and returns immediately with the value `true`,
setting the write lock hold count to one. If this lock has been
set to use a fair ordering policy then an available lock
will not be acquired if any other threads are
waiting for the write lock. This is in contrast to the `tryLock()` method. If you want a timed `tryLock`
that does permit barging on a fair lock then combine the
timed and un-timed forms together:
```
 
 if (lock.tryLock() ||
     lock.tryLock(timeout, unit)) {
   ...
 }
```
If the current thread already holds this lock then the
hold count is incremented by one and the method returns
`true`.If the lock is held by another thread then the current
thread becomes disabled for thread scheduling purposes and
lies dormant until one of three things happens:The write lock is acquired by the current thread; orSome other thread interrupts
the current thread; orThe specified waiting time elapsesIf the write lock is acquired then the value `true` is
returned and the write lock hold count is set to one.If the current thread:has its interrupted status set on entry to this method;
oris interrupted while
acquiring the write lock,then `InterruptedException` is thrown and the current
thread's interrupted status is cleared.If the specified waiting time elapses then the value
`false` is returned. If the time is less than or
equal to zero, the method will not wait at all.In this implementation, as this method is an explicit
interruption point, preference is given to responding to
the interrupt over normal or reentrant acquisition of the
lock, and over reporting the elapse of the waiting time.
Specified by:
`tryLock` in interface `Lock`
Parameters:
`timeout` - the time to wait for the write lock
`unit` - the time unit of the timeout argument
Returns:
`true` if the lock was free and was acquired
by the current thread, or the write lock was already held by the
current thread; and `false` if the waiting time
elapsed before the lock could be acquired.
Throws:
`InterruptedException` - if the current thread is interrupted
`NullPointerException` - if the time unit is null

#### unlock

```
public void unlock()
```
Attempts to release this lock.If the current thread is the holder of this lock then
the hold count is decremented. If the hold count is now
zero then the lock is released. If the current thread is
not the holder of this lock then `IllegalMonitorStateException` is thrown.
Specified by:
`unlock` in interface `Lock`
Throws:
`IllegalMonitorStateException` - if the current thread does not
hold this lock

#### newCondition

```
public Condition newCondition()
```
Returns a `Condition` instance for use with this
`Lock` instance.The returned `Condition` instance supports the same
usages as do the `Object` monitor methods (`wait`, `notify`, and `notifyAll`) when used with the built-in
monitor lock.If this write lock is not held when any `Condition` method is called then an `IllegalMonitorStateException` is thrown. (Read locks are
held independently of write locks, so are not checked or
affected. However it is essentially always an error to
invoke a condition waiting method when the current thread
has also acquired read locks, since other threads that
could unblock it will not be able to acquire the write
lock.)When the condition waiting
methods are called the write lock is released and, before
they return, the write lock is reacquired and the lock hold
count restored to what it was when the method was called.If a thread is interrupted while
waiting then the wait will terminate, an `InterruptedException` will be thrown, and the thread's
interrupted status will be cleared.Waiting threads are signalled in FIFO order.The ordering of lock reacquisition for threads returning
from waiting methods is the same as for threads initially
acquiring the lock, which is in the default case not specified,
but for fair locks favors those threads that have been
waiting the longest.
Specified by:
`newCondition` in interface `Lock`
Returns:
the Condition object

#### toString

```
public String toString()
```
Returns a string identifying this lock, as well as its lock
state. The state, in brackets includes either the String
`"Unlocked"` or the String `"Locked by"`
followed by the name of the owning thread.
Overrides:
`toString` in class `Object`
Returns:
a string identifying this lock, as well as its lock state

#### isHeldByCurrentThread

```
public boolean isHeldByCurrentThread()
```
Queries if this write lock is held by the current thread.
Identical in effect to `ReentrantReadWriteLock.isWriteLockedByCurrentThread()`.
Returns:
`true` if the current thread holds this lock and
`false` otherwise
Since:
1.6

#### getHoldCount

```
public int getHoldCount()
```
Queries the number of holds on this write lock by the current
thread. A thread has a hold on a lock for each lock action
that is not matched by an unlock action. Identical in effect
to `ReentrantReadWriteLock.getWriteHoldCount()`.
Returns:
the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread
Since:
1.6




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

