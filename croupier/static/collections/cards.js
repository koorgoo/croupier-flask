define([
  'backbone',
  'models/card'
], function(Backbone, Card) {
  var CardSet = Backbone.Collection.extend({
    model: Card,
    url: '/api/cards'
  });

  return CardSet;
});
