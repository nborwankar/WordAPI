from wordapi.api.handlers import (
    UrlTokenHandler, RequestTokenHandler, 
    UrlFrequencyHandler, RequestFrequencyHandler,
    TagCloudHandler,
    )

from django.conf.urls.defaults import patterns, url
from piston.resource import Resource

urlpatterns = patterns('',
  # tokenize the contents of the url passed in the request                       
  url(r'^tokenize/url\.(?P<emitter_format>.+)$', Resource(UrlTokenHandler)),
  # tokenize the contents of the content passed in the request
  url(r'^tokenize/request\.(?P<emitter_format>.+)$', Resource(RequestTokenHandler)),
  # calculate the token frequency of the contents at the url passed in                       
  url(r'^frequency/url\.(?P<emitter_format>.+)$', Resource(UrlFrequencyHandler)),
  # calculate the token frequency of the contents passed in                       
  url(r'^frequency/request\.(?P<emitter_format>.+)$', Resource(RequestFrequencyHandler)),
  # build a tag cloud from the contents passed in 
  url(r'^tagcloud\.(?P<emitter_format>.+)$', Resource(TagCloudHandler)),


)
