import { createRouter, createWebHistory } from 'vue-router';

import HomePage from './components/HomePage.vue';
import FormPage from './components/FormPage.vue';
import ConfirmPage from './components/ConfirmPage.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/form',
    name: 'Form',
    component: FormPage,
  },
  {
    path: '/confirm',
    name: 'Confirm',
    component: ConfirmPage,
  },
  

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
