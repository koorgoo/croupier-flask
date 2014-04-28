define([
  'underscore',
  'marionette',
  'text!templates/layouts/application.html',
], function(_, Marionette, Template) {
  var ApplicationLayout = Marionette.Layout.extend({
    el: 'body',
    template: _.template(Template),

    regions: {
      content: '.content'
    }
  });

  return ApplicationLayout;
});
