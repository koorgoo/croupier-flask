define([
  'underscore',
  'marionette',
  'text!templates/application.html',
], function(_, Marionette, Template) {
  return Marionette.ItemView.extend({
    template: _.template(Template)
  });
});
