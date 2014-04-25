requirejs.config({
  paths: {
    jquery:     'lib/zepto',
    deferred:   'lib/deferred',
    callbacks:  'lib/callbacks',
    underscore: 'lib/underscore',
    backbone:   'lib/backbone',
    marionette: 'lib/backbone.marionette',
    text:       'text',
  },
  shim: {
    jquery: {
      exports: '$'
    },
    deferred: {
      deps: ['jquery', 'callbacks'],
      exports: 'Deferred'
    },
    callbacks: {
      deps: ['jquery'],
      exports: 'Callbacks'
    },
    underscore: {
      exports: '_'
    },
    backbone: {
      deps: ['underscore', 'jquery'],
      exports: 'Backbone'
    },
    marionette: {
      deps: ['backbone', 'deferred'],
      exports: 'Backbone.Marionette'
    }
  }
});
