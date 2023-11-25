import { createRouter, createWebHistory } from 'vue-router'
import DashView from '../views/DashView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/dash',
      name: 'dash',
      component: DashView
    },
    {
      path: '/',
      name: 'landing',
      component: () => import("@/views/LandingView.vue")
    },
    {
      path: '/login',
      name: 'login',
      component: () => import("@/views/LoginView.vue")
    },
    {
      path: '/register',
      name: 'register',
      component: () => import("@/views/RegisterView.vue")
    },
  ]
})

export default router
