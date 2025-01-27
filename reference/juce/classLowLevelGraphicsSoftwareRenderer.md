A lowestcommondenominator implementation of LowLevelGraphicsContext that does all its rendering in memory.User code is not supposed to create instances of this class directly do all your rendering via the Graphics class instead.

Constructor & Destructor Documentation


◆ LowLevelGraphicsSoftwareRenderer() [1/2]


 LowLevelGraphicsSoftwareRenderer::LowLevelGraphicsSoftwareRenderer ( const Image & imageToRenderOnto ) 
 

Creates a context to render into an image.

◆ LowLevelGraphicsSoftwareRenderer() [2/2]


 LowLevelGraphicsSoftwareRenderer::LowLevelGraphicsSoftwareRenderer ( const Image & imageToRenderOnto, 
 
 Point< int > origin, 
 const RectangleList< int > & initialClip ) 

Creates a context to render into a clipped subsection of an image.

◆ ~LowLevelGraphicsSoftwareRenderer()


 LowLevelGraphicsSoftwareRenderer::~LowLevelGraphicsSoftwareRenderer ( ) override 
 

Destructor.