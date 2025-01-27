#### getQueuedReaderThreads

```
protected Collection<Thread> getQueuedReaderThreads()
```
Returns a collection containing threads that may be waiting to
acquire the read lock. Because the actual set of threads may
change dynamically while constructing this result, the returned
collection is only a best-effort estimate. The elements of the
returned collection are in no particular order. This method is
designed to facilitate construction of subclasses that provide
more extensive lock monitoring facilities.
Returns:
the collection of threads

