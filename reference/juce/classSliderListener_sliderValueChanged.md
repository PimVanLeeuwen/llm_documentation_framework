#### sliderValueChanged()


template<typename Emitter > 

 virtual void SliderListener< Emitter >::sliderValueChanged ( Emitter \* ) pure virtual 
 

Called when the slider's value is changed.This may be caused by dragging it, or by typing in its text entry box, or by a call to Slider::setValue().You can find out the new value using Slider::getValue().See alsoSlider::valueChanged