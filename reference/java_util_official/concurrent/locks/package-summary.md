

java.util.concurrent.locks (Java Platform SE 8 )





<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="java.util.concurrent.locks (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->

JavaScript is disabled on your browser.


Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
<!--
allClassesLink = document.getElementById("allclasses\_navbar\_top");
if(window==top) {
allClassesLink.style.display = "block";
}
else {
allClassesLink.style.display = "none";
}
//-->




Package java.util.concurrent.locks
Interfaces and classes providing a framework for locking and waiting
for conditions that is distinct from built-in synchronization and
monitors.
See: Description

Interface Summary InterfaceDescriptionCondition`Condition` factors out the `Object` monitor
methods (`wait`, `notify`
and `notifyAll`) into distinct objects to
give the effect of having multiple wait-sets per object, by
combining them with the use of arbitrary `Lock` implementations.Lock`Lock` implementations provide more extensive locking
operations than can be obtained using `synchronized` methods
and statements.ReadWriteLockA `ReadWriteLock` maintains a pair of associated `locks`, one for read-only operations and one for writing.

Class Summary ClassDescriptionAbstractOwnableSynchronizerA synchronizer that may be exclusively owned by a thread.AbstractQueuedLongSynchronizerA version of `AbstractQueuedSynchronizer` in
which synchronization state is maintained as a `long`.AbstractQueuedSynchronizerProvides a framework for implementing blocking locks and related
synchronizers (semaphores, events, etc) that rely on
first-in-first-out (FIFO) wait queues.LockSupportBasic thread blocking primitives for creating locks and other
synchronization classes.ReentrantLockA reentrant mutual exclusion `Lock` with the same basic
behavior and semantics as the implicit monitor lock accessed using
`synchronized` methods and statements, but with extended
capabilities.ReentrantReadWriteLockAn implementation of `ReadWriteLock` supporting similar
semantics to `ReentrantLock`.ReentrantReadWriteLock.ReadLockThe lock returned by method `ReentrantReadWriteLock.readLock()`.ReentrantReadWriteLock.WriteLockThe lock returned by method `ReentrantReadWriteLock.writeLock()`.StampedLockA capability-based lock with three modes for controlling read/write
access.

Package java.util.concurrent.locks DescriptionInterfaces and classes providing a framework for locking and waiting
for conditions that is distinct from built-in synchronization and
monitors. The framework permits much greater flexibility in the use of
locks and conditions, at the expense of more awkward syntax.The `Lock` interface supports
locking disciplines that differ in semantics (reentrant, fair, etc),
and that can be used in non-block-structured contexts including
hand-over-hand and lock reordering algorithms. The main implementation
is `ReentrantLock`.The `ReadWriteLock` interface
similarly defines locks that may be shared among readers but are
exclusive to writers. Only a single implementation, `ReentrantReadWriteLock`, is provided, since
it covers most standard usage contexts. But programmers may create
their own implementations to cover nonstandard requirements.The `Condition` interface
describes condition variables that may be associated with Locks.
These are similar in usage to the implicit monitors accessed using
`Object.wait`, but offer extended capabilities.
In particular, multiple `Condition` objects may be associated
with a single `Lock`. To avoid compatibility issues, the
names of `Condition` methods are different from the
corresponding `Object` versions.The `AbstractQueuedSynchronizer`
class serves as a useful superclass for defining locks and other
synchronizers that rely on queuing blocked threads. The `AbstractQueuedLongSynchronizer` class
provides the same functionality but extends support to 64 bits of
synchronization state. Both extend class `AbstractOwnableSynchronizer`, a simple
class that helps record the thread currently holding exclusive
synchronization. The `LockSupport`
class provides lower-level blocking and unblocking support that is
useful for those developers implementing their own customized lock
classes.
Since:
1.5



Skip navigation links

OverviewPackageClassUseTreeDeprecatedIndexHelpJava™ PlatformStandard Ed. 8

Prev PackageNext PackageFramesNo FramesAll Classes
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

