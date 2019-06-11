import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Info from '@/components/Info'

Vue.use(Router)

/* For reference
{
  path: '/',
  name: 'HelloWorld',
  component: HelloWorld
} */

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Main
    },
    {
      path: '/info',
      name: 'info',
      component: Info
    },
  ]
})