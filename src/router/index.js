import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginPage from '@/components/LoginPage.vue'
import SignUpPage from '@/components/SignUpPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/TestView.vue')
  },
  {
<<<<<<< HEAD
    path: '/search',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  {
=======
>>>>>>> d52ebe3d423373a3d85bbdd7eee69a2a7be68d05
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
