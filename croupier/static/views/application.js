define([
  'underscore',
  'marionette',
  'text!templates/application.html',
], function(_, Marionette, Template) {
  return window.AppView = Marionette.ItemView.extend({
    template: _.template(Template)
  });
});
