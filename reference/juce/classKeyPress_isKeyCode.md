#### isKeyCode()


 bool KeyPress::isKeyCode ( int keyCodeToCompare ) const noexcept 
 

Checks whether the KeyPress's key is the same as the one provided, without checking the modifiers.The values for key codes can either be one of the special constants defined in this class, or an 8bit character code.See alsogetKeyCode Referenced by TextEditorKeyMapper< CallbackClass >::invokeKeyFunction().