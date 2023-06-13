import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginPage from '@/components/LoginPage.vue'
import SignUpPage from '@/components/SignUpPage.vue'
import NaverLogin from '../views/NaverLogin.vue'
import Todo from '../views/Todo.vue'
import Prof from '../views/Prof.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/naverlogin',
    name: 'NaverLogin',
    component: NaverLogin
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/TestView.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpPage
  },
  {
    path: '/PageMenu',
    name: 'PageMenu',
    component: () => import('../components/PageMenu.vue')
  },
  {
    path: '/rate',
    name: 'rate',
    component: () => import('../views/ExchangeRate.vue')
  },
  {
    path: '/Todo',
    name: 'Todo',
    component: Todo
  },
  {
    path: '/Prof',
    name: 'Prof',
    component: Prof
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
