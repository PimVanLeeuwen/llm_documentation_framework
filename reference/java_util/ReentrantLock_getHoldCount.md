#### getHoldCount

```
public int getHoldCount()
```
Queries the number of holds on this lock by the current thread.A thread has a hold on a lock for each lock action that is not
matched by an unlock action.The hold count information is typically only used for testing and
debugging purposes. For example, if a certain section of code should
not be entered with the lock already held then we can assert that
fact:
```
 
 class X {
   ReentrantLock lock = new ReentrantLock();
   // ...
   public void m() {
     assert lock.getHoldCount() == 0;
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
the number of holds on this lock by the current thread,
or zero if this lock is not held by the current thread

