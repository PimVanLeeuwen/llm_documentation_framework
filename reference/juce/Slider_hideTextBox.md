#### hideTextBox()


 void Slider::hideTextBox ( bool discardCurrentEditorContents ) 
 

If the textbox currently has focus and is being edited, this resets it and takes keyboard focus away from it.Parameters

 discardCurrentEditorContents if true, the slider's value will be left unchanged; if false, the current contents of the text editor will be used to set the slider position before it is hidden.