#### useFullscreenWhenOneDocument()


 void MultiDocumentPanel::useFullscreenWhenOneDocument ( bool shouldUseTabs ) 
 

Sets an option to make the document fullscreen if there's only one document open.If set to true, then if there's only one document, it'll fill the whole of this component without tabs or a window border. If false, then tabs or a window will always be shown, even if there's only one document. If there's more than one document open, then this option makes no difference.