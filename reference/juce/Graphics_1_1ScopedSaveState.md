Uses RAII to save and restore the state of a graphics context.On construction, this calls Graphics::saveState(), and on destruction it calls Graphics::restoreState() on the Graphics object that you supply.

Constructor & Destructor Documentation


◆ ScopedSaveState()


 Graphics::ScopedSaveState::ScopedSaveState ( Graphics & ) 
 



◆ ~ScopedSaveState()


 Graphics::ScopedSaveState::~ScopedSaveState ( ) 
 