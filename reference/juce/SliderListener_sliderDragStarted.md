#### sliderDragStarted()


template<typename Emitter > 

 virtual void SliderListener< Emitter >::sliderDragStarted ( Emitter \* ) virtual 
 

Called when the slider is about to be dragged.This is called when a drag begins, then it's followed by multiple calls to sliderValueChanged(), and then sliderDragEnded() is called after the user lets go.See alsosliderDragEnded, Slider::startedDragging