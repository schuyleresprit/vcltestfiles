var gulp = require('gulp');

var css = require('css');
var javascript = require('javascript');
var json = require('json');

// Define tasks
function css() {
  gulp.src('css/styles.css')
  .pipe(dest('output'));
}

function javascript() {
  gulp.src('js/visTestvcl.js')
  .pipe(dest('output'));
}

function json() {
  gulp.src('package.json')
  .pipe(dest('output'));
}

function watch() {
  gulp.watch('styles/**/*.css', ['processCSS']);
}
//const { series, parallel } = require('gulp');
//const { src, dest } = require('gulp');

//function clean(cb) {
  // body omitted
  //cb();
//}

//function css() {
  // body omitted
 // return src('css/style.css')
//    .pipe(dest('output'));

//
//function javascript() {
    //return src('js/visTestvcl.js')
      //.pipe(dest('output'));

//}

//exports.build = series(clean, parallel(css, javascript));
