#### shareImagesScoped()


 static ScopedMessageBox ContentSharer::shareImagesScoped ( const Array< Image > & images, std::unique\_ptr< ImageFileFormat > format, Callback callback, Component \* parent = nullptr ) staticnodiscard 
 

A convenience function to share an image.This is useful when you have images loaded in memory. The images will be written to temporary files first, so if you have the images in question stored on disk already call shareFiles() instead. By default, images will be saved to PNG files, but you can supply a custom ImageFileFormat to override this. The custom file format will be owned and deleted by the sharer. e.g.Graphics g (myImage);
g.setColour (Colours::green);
g.fillEllipse (20, 20, 300, 200);
Array<Image> images;
images.add (myImage);
ContentSharer::getInstance()>shareImages (images, myCallback);
ArrayHolds a resizable array of primitive or copybyvalue objects.Definition juce\_Array.h:71
Array::addvoid add(const ElementType &newElement)Appends a new element at the end of the array.Definition juce\_Array.h:433
GraphicsA graphics context, used for drawing a component or image.Definition juce\_GraphicsContext.h:57
Colours::greenconst Colour greenDefinition juce\_Colours.h:102
Upon completion you will receive a callback with a sharing result. Note: Sadly on Android the returned success flag may be wrong as there is no standard way the sharing targets report if the sharing operation succeeded. Also, the optional error message is always empty on Android.Parameters

 images the images to share 
 
 format the file format to use when saving the images. If no format is provided, a sensible default will be used. 
 callback a callback that will be called on the main thread when the sharing session ends 
 parent the component that should be used to host the sharing view