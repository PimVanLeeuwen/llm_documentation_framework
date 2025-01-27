#### setIcon()


 void DocumentWindow::setIcon ( const Image & imageToUse ) 
 

Sets an icon to show in the title bar, next to the title.A copy is made internally of the image, so the caller can delete the image after calling this. If an empty Image is passedin, any existing icon will be removed.