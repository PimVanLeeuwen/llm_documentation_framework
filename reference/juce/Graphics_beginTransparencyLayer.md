#### beginTransparencyLayer()


 void Graphics::beginTransparencyLayer ( float layerOpacity ) 
 

Begins rendering to an offscreen bitmap which will later be flattened onto the current context with the given opacity.The context uses an internal stack of temporary image layers to do this. When you've finished drawing to the layer, call endTransparencyLayer() to complete the operation and composite the finished layer. Every call to beginTransparencyLayer() MUST be matched by a corresponding call to endTransparencyLayer()!This call also saves the current state, and endTransparencyLayer() restores it.