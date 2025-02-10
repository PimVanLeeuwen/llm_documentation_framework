#### setIconImage()


 void SystemTrayIconComponent::setIconImage ( const Image & colourImage, 
 
 const Image & templateImage ) 

Changes the image shown in the taskbar.On Windows and Linux a full colour Image is used as an icon. On macOS a template image is used, where all nontransparent regions will be rendered in a monochrome colour selected dynamically by the operating system.Parameters

 colourImage An colour image to use as an icon on Windows and Linux 
 
 templateImage A template image to use as an icon on macOS