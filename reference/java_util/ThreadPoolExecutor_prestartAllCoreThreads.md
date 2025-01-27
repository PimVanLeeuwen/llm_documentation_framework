#### prestartAllCoreThreads

```
public int prestartAllCoreThreads()
```
Starts all core threads, causing them to idly wait for work. This
overrides the default policy of starting core threads only when
new tasks are executed.
Returns:
the number of threads started

