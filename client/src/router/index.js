import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../pages/Home.vue'
import About from '../pages/About'
import User from '../pages/User'

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/user', component: User },
]

export const router = new VueRouter({
  routes: routes
})