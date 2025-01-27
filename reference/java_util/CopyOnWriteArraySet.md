```
public class CopyOnWriteArraySet<E>
extends AbstractSet<E>
implements Serializable
```
A `Set` that uses an internal `CopyOnWriteArrayList`
for all of its operations. Thus, it shares the same basic properties:It is best suited for applications in which set sizes generally
stay small, read-only operations
vastly outnumber mutative operations, and you need
to prevent interference among threads during traversal.It is thread-safe.Mutative operations (`add`, `set`, `remove`, etc.)
are expensive since they usually entail copying the entire underlying
array.Iterators do not support the mutative `remove` operation.Traversal via iterators is fast and cannot encounter
interference from other threads. Iterators rely on
unchanging snapshots of the array at the time the iterators were
constructed.Sample Usage. The following code sketch uses a
copy-on-write set to maintain a set of Handler objects that
perform some action upon state updates.
```
 
 class Handler { void handle(); ... }

 class X {
   private final CopyOnWriteArraySet<Handler> handlers
     = new CopyOnWriteArraySet<Handler>();
   public void addHandler(Handler h) { handlers.add(h); }

   private long internalState;
   private synchronized void changeState() { internalState = ...; }

   public void update() {
     changeState();
     for (Handler handler : handlers)
       handler.handle();
   }
 }
```
This class is a member of the
Java Collections Framework.
Since:
1.5
See Also:
`CopyOnWriteArrayList`,
Serialized Form
