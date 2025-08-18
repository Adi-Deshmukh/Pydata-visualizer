



analyzer_registry = {}

def register_analyzer(vision_type):
    """
    This is the outer function that takes the vision_type as an argument.
    It returns the actual decorator.
    """
    def decorator(analyzer_function):
        """
        This is the inner function (the real decorator).
        It takes the function to be decorated and registers it.
        """
        # The core logic: add the function to our registry
        analyzer_registry[vision_type] = analyzer_function
        
        # Return the original, unmodified function
        return analyzer_function
        
    # The outer function returns the inner function
    return decorator

