define(function() {
  var run = function() {
    test( "hello test", function() {
      ok( 1 == "1", "Passed!" );
    });
  };

  return { run: run }
});
