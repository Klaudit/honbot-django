'use strict';

var gulp = require('gulp');

gulp.task('watch', ['styles'] ,function () {
  gulp.watch('src/{app,components}/**/*.scss', ['styles']);
  gulp.watch('src/{app,components}/**/*.js', ['scripts']);
  gulp.watch('bower.json', ['wiredep']);
});
