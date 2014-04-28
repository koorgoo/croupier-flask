define([
  'marionette',
  'layouts/application',
  'views/card'
], function(Marionette, AppLayout, CardView) {
  var app = new Marionette.Application();

  app.addInitializer(function(options) {
    var layout = new AppLayout();
    var card = new CardView();

    layout.render();
    layout.content.show(card);
  });

  return app;
});
