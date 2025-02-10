#### addSettingsPage() [2/2]


 void PreferencesPanel::addSettingsPage ( const String & pageTitle, 
 
 const void \* imageData, 
 int imageDataSize ) 

Creates a page using a set of drawables to define the page's icon.The other version of this method gives you more control over the icon, but this one is much easier if you're just loading it from a file.Parameters

 pageTitle the name of this preferences page you'll need to make sure your createComponentForPage() method creates a suitable component when it is passed this name 
 
 imageData a block of data containing an image file, e.g. a jpeg, png or gif. For this to look good, you'll probably want to use a nice transparent png file. 
 imageDataSize the size of the image data, in bytes