

Uses of Package java.util.concurrent.locks (Java Platform SE 8 )




<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="Uses of Package java.util.concurrent.locks (Java Platform SE 8 )";
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




Uses of Packagejava.util.concurrent.locks

Packages that use java.util.concurrent.locks PackageDescriptionjava.util.concurrent.locksInterfaces and classes providing a framework for locking and waiting
for conditions that is distinct from built-in synchronization and
monitors.

Classes in java.util.concurrent.locks used by java.util.concurrent.locks Class and DescriptionAbstractOwnableSynchronizer
A synchronizer that may be exclusively owned by a thread.AbstractQueuedLongSynchronizer.ConditionObject
Condition implementation for a `AbstractQueuedLongSynchronizer` serving as the basis of a `Lock` implementation.AbstractQueuedSynchronizer.ConditionObject
Condition implementation for a `AbstractQueuedSynchronizer` serving as the basis of a `Lock` implementation.Condition
`Condition` factors out the `Object` monitor
methods (`wait`, `notify`
and `notifyAll`) into distinct objects to
give the effect of having multiple wait-sets per object, by
combining them with the use of arbitrary `Lock` implementations.Lock
`Lock` implementations provide more extensive locking
operations than can be obtained using `synchronized` methods
and statements.ReadWriteLock
A `ReadWriteLock` maintains a pair of associated `locks`, one for read-only operations and one for writing.ReentrantReadWriteLock
An implementation of `ReadWriteLock` supporting similar
semantics to `ReentrantLock`.ReentrantReadWriteLock.ReadLock
The lock returned by method `ReentrantReadWriteLock.readLock()`.ReentrantReadWriteLock.WriteLock
The lock returned by method `ReentrantReadWriteLock.writeLock()`.


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

