/**
 * NOTE: This javascript is not compiled for older browers.
 * After modifying this file, use snowpack. https://snowpack.dev
 */

try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');
    require('bootstrap');
} catch (e) { }

window.axios = require('axios')
window.moment = require('moment')
// axios.defaults.headers.common['content-type'] = 'application/x-www-form-urlencoded;charset=utf-8'
window.Vue = require('vue').default;

Vue.config.devtools = true

Vue.component('CsvUploader', require('./components/CsvUploader.vue').default)
Vue.component('BootstrapCard', require('./components/BootstrapCard.vue').default)
Vue.component('GraphWizard', require('./components/GraphWizard.vue').default)
Vue.component('ThemeOverlay', require('./components/ThemeOverlay.vue').default)
Vue.component('ThemeSwitcher', require('./components/ThemeSwitcher.vue').default)


const app = new Vue({
    el: '#app'
})

