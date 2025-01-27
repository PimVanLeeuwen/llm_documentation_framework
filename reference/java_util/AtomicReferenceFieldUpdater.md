```
public abstract class AtomicReferenceFieldUpdater<T,V>
extends Object
```
A reflection-based utility that enables atomic updates to
designated `volatile` reference fields of designated
classes. This class is designed for use in atomic data structures
in which several reference fields of the same node are
independently subject to atomic updates. For example, a tree node
might be declared as
```
 
 class Node {
   private volatile Node left, right;

   private static final AtomicReferenceFieldUpdater<Node, Node> leftUpdater =
     AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "left");
   private static AtomicReferenceFieldUpdater<Node, Node> rightUpdater =
     AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "right");

   Node getLeft() { return left; }
   boolean compareAndSetLeft(Node expect, Node update) {
     return leftUpdater.compareAndSet(this, expect, update);
   }
   // ... and so on
 }
```
Note that the guarantees of the `compareAndSet`
method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of
`compareAndSet` and `set` on the same updater.
Since:
1.5
