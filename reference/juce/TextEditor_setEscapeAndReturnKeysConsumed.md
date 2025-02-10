#### setEscapeAndReturnKeysConsumed()


 void TextEditor::setEscapeAndReturnKeysConsumed ( bool shouldBeConsumed ) noexcept 
 

This can be used to change whether escape and return keypress events are propagated up to the parent component.The default here is true, meaning that these events are not allowed to reach the parent, but you may want to allow them through so that they can trigger other actions, e.g. closing a dialog box, etc.