define([
  'marionette',
  'views/application',
], function(Marionette, AppView) {
  var app = new Marionette.Application();

  app.addRegions({
    bodyRegion: 'body'
  });

  app.addInitializer(function(options) {
    app.bodyRegion.show(new AppView());
  });

  return app;
});
