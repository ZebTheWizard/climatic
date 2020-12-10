/**
 * NOTE: This javascript is not compiled for older browers.
 * After modifying this file, use snowpack. https://snowpack.dev
 */

try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (e) { }

window.Vue = require('vue').default;

Vue.component('CsvUploader', require('./components/CsvUploader.vue').default)
Vue.component('BootstrapCard', require('./components/BootstrapCard.vue').default)
Vue.component('GraphWizard', require('./components/GraphWizard.vue').default)


const app = new Vue({
    el: '#app'
})