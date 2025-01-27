#### reset

```
public void reset()
```
Resets variables maintaining updates to the identity value.
This method may be a useful alternative to creating a new
updater, but is only effective if there are no concurrent
updates. Because this method is intrinsically racy, it should
only be used when it is known that no threads are concurrently
updating.

