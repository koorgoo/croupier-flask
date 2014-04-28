define([
  'marionette',
  'layouts/application',
  'collections/cards',
  'views/card'
], function(Marionette, AppLayout, CardSet, CardView) {
  var app = new Marionette.Application();

  app.addInitializer(function(options) {
    var layout = new AppLayout();
    var cards = new CardSet();
    var view = new CardView({ collection: cards });

    cards.fetch().done(function() {
      layout.render();
      layout.content.show(view);
    });
  });

  return app;
});
