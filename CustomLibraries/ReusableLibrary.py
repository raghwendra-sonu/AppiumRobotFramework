def _is_ios(self):
    return self._is_platform('ios')

def _is_android(self):
    return self._is_platform('android')
    
def _is_element_present(self, locator):
    application = self._current_application()
    elements = self._element_finder.find(application, locator, None)
    return len(elements) > 0

def _is_visible(self, locator):
    element = self._element_find(locator, True, False)
    if element is not None:
        return element.is_displayed()
    return None

