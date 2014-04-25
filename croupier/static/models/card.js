define(['backbone'], function(Backbone) {
  var Card = Backbone.Model.extend({
    defaults: { front: '', back:  '' }
  });

  return Card;
});
