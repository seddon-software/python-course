"use strict";

(function () {
  function getViewerContent() {
    const elem = document.getElementById('analyticsignal.preview-pdf')
    if (elem) {
      return elem.getAttribute('content')
    }
    throw new Error('Could not find preview content.')
  }

  window.addEventListener('load', function () {
    const content_path = getViewerContent()    
    PDFViewerApplication.open(content_path)

    window.addEventListener('message', function () {
      window.PDFViewerApplication.open(content_path)
    });
  }, { once:true });

  window.onerror = function () {
    const msg = document.createElement('body')
    msg.innerText = 'An error occurred reading the document. Please try again.'
    document.body = msg
  }
}());