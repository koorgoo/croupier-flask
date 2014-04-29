define([
  'collections/cards',
  'views/card',
  'qunit',
], function(CardSet, CardView) {
  var cards, view;

  module('CardView', {
    setup: function() {
      cards = new CardSet([
        { id: 1, front: '1 + 2 = ?', back: '3' },
        { id: 2, front: '2 + 3 = ?', back: '5' }
      ]);

      view = new CardView({ collection: cards });
      view.render();
    },
    teardown: function() {
      view.close();
      cards.reset();
    }
  });

  test('shows first card on render', function() {
    equal(view.model.get('id'), 1);
  });

  test('shows next card on goNext()', function() {
    view.goNext();
    equal(view.model.get('id'), 2);
  });

  test('shows first card after last card`', function() {
    view.goNext();
    view.goNext();
    equal(view.model.get('id'), 1);
  });
});
