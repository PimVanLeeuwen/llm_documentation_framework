#### update

```
void update(Observable o,
            Object arg)
```
This method is called whenever the observed object is changed. An
application calls an Observable object's
`notifyObservers` method to have all the object's
observers notified of the change.
Parameters:
`o` - the observable object.
`arg` - an argument passed to the `notifyObservers`
method.




