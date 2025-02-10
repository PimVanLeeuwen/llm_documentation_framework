#### setPaintingIsUnclipped()


 void Component::setPaintingIsUnclipped ( bool shouldPaintWithoutClipping ) noexcept 
 

This allows you to indicate that this component doesn't require its graphics context to be clipped when it is being painted.Most people will never need to use this setting, but in situations where you have a very large number of simple components being rendered, and where they are guaranteed never to do any drawing beyond their own boundaries, setting this to true will reduce the overhead involved in clipping the graphics context that gets passed to the component's paint() callback.If you enable this mode, you'll need to make sure your paint method doesn't call anything like Graphics::fillAll(), and doesn't draw beyond the component's bounds, because that'll produce artifacts. This option will have no effect on components that contain any child components.