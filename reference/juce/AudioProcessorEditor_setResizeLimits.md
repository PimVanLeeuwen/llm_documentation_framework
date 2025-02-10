#### setResizeLimits()


 void AudioProcessorEditor::setResizeLimits ( int newMinimumWidth, int newMinimumHeight, int newMaximumWidth, int newMaximumHeight ) noexcept 
 

This sets the maximum and minimum sizes for the window.If the window's current size is outside these limits, it will be resized to make sure it's within them.If you pass in a different minimum and maximum size, this will mark the editor as resizable by the host.A direct call to setBounds() will bypass any constraint checks, but when the window is dragged by the user or resized by other indirect means, the constrainer will limit the numbers involved.Note that if you have set a custom constrainer for this editor then this will have no effect, and if you have removed the constrainer with `setConstrainer (nullptr);` then this will readd the default constrainer with the new limits.See alsosetResizable