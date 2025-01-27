#### onStart

```
protected void onStart()
```
Initializes internal state after construction but before
processing any tasks. If you override this method, you must
invoke `super.onStart()` at the beginning of the method.
Initialization requires care: Most fields must have legal
default values, to ensure that attempted accesses from other
threads work correctly even before this thread starts
processing tasks.

