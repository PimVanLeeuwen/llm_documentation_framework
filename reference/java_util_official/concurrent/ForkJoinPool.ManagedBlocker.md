

ForkJoinPool.ManagedBlocker (Java Platform SE 8 )







<!--
try {
if (location.href.indexOf('is-external=true') == -1) {
parent.document.title="ForkJoinPool.ManagedBlocker (Java Platform SE 8 )";
}
}
catch(err) {
}
//-->
var methods = {"i0":6,"i1":6};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],4:["t3","Abstract Methods"]};
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
java.util.concurrentInterface ForkJoinPool.ManagedBlocker
Enclosing class:
ForkJoinPool


```
public static interface ForkJoinPool.ManagedBlocker
```
Interface for extending managed parallelism for tasks running
in `ForkJoinPool`s.A `ManagedBlocker` provides two methods. Method
`isReleasable()` must return `true` if blocking is
not necessary. Method `block()` blocks the current thread
if necessary (perhaps internally invoking `isReleasable`
before actually blocking). These actions are performed by any
thread invoking `ForkJoinPool.managedBlock(ManagedBlocker)`.
The unusual methods in this API accommodate synchronizers that
may, but don't usually, block for long periods. Similarly, they
allow more efficient internal handling of cases in which
additional workers may be, but usually are not, needed to
ensure sufficient parallelism. Toward this end,
implementations of method `isReleasable` must be amenable
to repeated invocation.For example, here is a ManagedBlocker based on a
ReentrantLock:
```
 
 class ManagedLocker implements ManagedBlocker {
   final ReentrantLock lock;
   boolean hasLock = false;
   ManagedLocker(ReentrantLock lock) { this.lock = lock; }
   public boolean block() {
     if (!hasLock)
       lock.lock();
     return true;
   }
   public boolean isReleasable() {
     return hasLock || (hasLock = lock.tryLock());
   }
 }
```
Here is a class that possibly blocks waiting for an
item on a given queue:
```
 
 class QueueTaker<E> implements ManagedBlocker {
   final BlockingQueue<E> queue;
   volatile E item = null;
   QueueTaker(BlockingQueue<E> q) { this.queue = q; }
   public boolean block() throws InterruptedException {
     if (item == null)
       item = queue.take();
     return true;
   }
   public boolean isReleasable() {
     return item != null || (item = queue.poll()) != null;
   }
   public E getItem() { // call after pool.managedBlock completes
     return item;
   }
 }
```

### Method Summary

All Methods Instance Methods Abstract Methods Modifier and TypeMethod and Description`boolean``block()`
Possibly blocks the current thread, for example waiting for
a lock or condition.`boolean``isReleasable()`
Returns `true` if blocking is unnecessary.

### Method Detail

#### block

```
boolean block()
       throws InterruptedException
```
Possibly blocks the current thread, for example waiting for
a lock or condition.
Returns:
`true` if no additional blocking is necessary
(i.e., if isReleasable would return true)
Throws:
`InterruptedException` - if interrupted while waiting
(the method is not required to do so, but is allowed to)

#### isReleasable

```
boolean isReleasable()
```
Returns `true` if blocking is unnecessary.
Returns:
`true` if blocking is unnecessary




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

