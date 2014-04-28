define([
  'underscore',
  'marionette',
  'text!templates/card.html'
], function(_, Marionette, Template) {
  var CardView = Marionette.ItemView.extend({
    template: _.template(Template)
  });

  return CardView;
});
