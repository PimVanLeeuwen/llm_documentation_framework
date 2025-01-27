#### isHeldByCurrentThread

```
public boolean isHeldByCurrentThread()
```
Queries if this lock is held by the current thread.Analogous to the `Thread.holdsLock(Object)` method for
built-in monitor locks, this method is typically used for
debugging and testing. For example, a method that should only be
called while a lock is held can assert that this is the case:
```
 
 class X {
   ReentrantLock lock = new ReentrantLock();
   // ...

   public void m() {
       assert lock.isHeldByCurrentThread();
       // ... method body
   }
 }
```
It can also be used to ensure that a reentrant lock is used
in a non-reentrant manner, for example:
```
 
 class X {
   ReentrantLock lock = new ReentrantLock();
   // ...

   public void m() {
       assert !lock.isHeldByCurrentThread();
       lock.lock();
       try {
           // ... method body
       } finally {
           lock.unlock();
       }
   }
 }
```

Returns:
`true` if current thread holds this lock and
`false` otherwise

