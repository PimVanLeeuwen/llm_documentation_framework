#### countDown

```
public void countDown()
```
Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.If the current count equals zero then nothing happens.

