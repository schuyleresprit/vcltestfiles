var gulp = require('gulp');

const { series, parallel } = require('gulp');
const { src, dest } = require('gulp');

function clean(cb) {
  // body omitted
 cb();
}

function css() {
  // body omitted
  return src('css/style.css')
    .pipe(dest('output'));
}
//
function javascript() {
    return src('js/visTestvcl.js')
      .pipe(dest('output'));

}

exports.build = series(clean, parallel(css, javascript));
