#### isCurrentlyModal()


 bool Component::isCurrentlyModal ( bool onlyConsiderForemostModalComponent = true ) const noexcept 
 

Returns true if this component is the modal one.It's possible to have nested modal components, e.g. a popup dialog box that launches another popup. If onlyConsiderForemostModalComponent is true then isCurrentlyModal will only return true for the one at the top of the stack. If onlyConsiderForemostModalComponent is false then isCurrentlyModal will return true for any modal component in the stack.See alsogetCurrentlyModalComponent