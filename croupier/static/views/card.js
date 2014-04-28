define([
  'underscore',
  'marionette',
  'text!templates/card.html'
], function(_, Marionette, Template) {
  var CardView = Marionette.ItemView.extend({
    template: _.template(Template),

    render: function() {
      this.$el.html(this.template());
      this.goNext();

      return this;
    },

    ui: {
      toggle  : '.toggle',
      front   : '.front',
      back    : '.back'
    },

    events: {
      'click .toggle'  : 'toggleBack',
      'click .go'      : 'goNext'
    },

    toggleBack: function() {
      this.$('.toggle').toggleClass('hidden');
      this.$('.front').toggleClass('muted');
      this.$('.back').toggleClass('hidden');

      this.toggled = this.$('.toggle').hasClass('hidden');
    },

    goNext: function() {
      if (this.toggled) this.toggleBack();

      this.index || (this.index = 0);
      if (this.index == this.collection.length) 
        this.index = 0;

      this.model = this.collection.at(this.index);
      this.update();

      this.index++;
    },

    update: function() {
      this.$('.front').text(this.model.get('front'));
      this.$('.back').text(this.model.get('back'));
    }
  });

  return CardView;
});
