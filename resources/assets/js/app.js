/**
 * NOTE: This javascript is not compiled for older browers.
 * After modifying this file, use snowpack. https://snowpack.dev
 */


try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (e) { }