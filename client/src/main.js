import Vue from 'vue'
import App from './App.vue'
import { store } from './store'
import './assets/css/main.css';

Vue.config.productionTip = false

new Vue({
  el: '#app',
  store: store,
  render: h => h(App),
}).$mount('#app')
