#### isInitialising()


 bool JUCEApplicationBase::isInitialising ( ) const noexcept 
 

Returns true if the application hasn't yet completed its initialise() method and entered the main event loop.This is handy for things like splash screens to know when the app's upandrunning properly.