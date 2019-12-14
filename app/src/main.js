import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueSkycons from 'vue-skycon'

Vue.config.productionTip = false
Vue.use(VueSkycons)

new Vue({
  el: '#app',
  vuetify,
  render: h => h(App)
}).$mount('#app')
