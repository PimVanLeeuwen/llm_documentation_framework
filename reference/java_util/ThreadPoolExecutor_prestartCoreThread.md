#### prestartCoreThread

```
public boolean prestartCoreThread()
```
Starts a core thread, causing it to idly wait for work. This
overrides the default policy of starting core threads only when
new tasks are executed. This method will return `false`
if all core threads have already been started.
Returns:
`true` if a thread was started

