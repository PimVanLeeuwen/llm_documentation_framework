#### isActiveWindow()


 bool TopLevelWindow::isActiveWindow ( ) const noexcept 
 

True if this is currently the TopLevelWindow that is actively being used.This isn't quite the same as having keyboard focus, because the focus may be on a child component or a temporary popup menu, etc, while this window is still considered to be active.See alsoactiveWindowStatusChanged