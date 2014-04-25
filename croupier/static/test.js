requirejs.config({
  paths: {
    qunit: 'lib/qunit'
  },
  shim: {
    qunit: {
      exports: 'QUnit',
      init: function() {
        QUnit.config.autostart = false;
      }
    }
  }
});

require([
  'qunit',
  'tests/foo'
], function(QUnit) {
  QUnit.load();
  QUnit.start();
});
