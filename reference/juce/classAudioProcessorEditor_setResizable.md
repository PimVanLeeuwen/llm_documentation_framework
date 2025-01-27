#### setResizable()


 void AudioProcessorEditor::setResizable ( bool allowHostToResize, 
 
 bool useBottomRightCornerResizer ) 

Sets whether the editor is resizable by the host and/or user.Parameters

 allowHostToResize whether the editor's parent window can be resized by the host. Even if this is false, you can still resize your window yourself by calling setBounds (for example, when a user clicks on a button in your editor to drop out a panel) which will bypass any resizable/constraints checks. 
 
 useBottomRightCornerResizer if this is true, a ResizableCornerComponent will be added to the editor's bottomright to allow the user to resize the editor regardless of the value of `allowHostToResize`. 



See alsosetResizeLimits, isResizable