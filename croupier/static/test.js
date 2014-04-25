requirejs.config({
  paths: {
    qunit: 'lib/qunit'
  },
  shim: {
    qunit: {
      exports: 'QUnit',
      init: function() {
        QUnit.config.autoload = false;
        QUnit.config.autostart = false;
      }
    }
  }
});

require([
  'qunit',
  'tests/foo'
], function(QUnit, foo) {
  foo.run();

  QUnit.load();
  QUnit.start();
});
