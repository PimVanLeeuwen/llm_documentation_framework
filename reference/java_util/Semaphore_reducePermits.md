#### reducePermits

```
protected void reducePermits(int reduction)
```
Shrinks the number of available permits by the indicated
reduction. This method can be useful in subclasses that use
semaphores to track resources that become unavailable. This
method differs from `acquire` in that it does not block
waiting for permits to become available.
Parameters:
`reduction` - the number of permits to remove
Throws:
`IllegalArgumentException` - if `reduction` is negative

