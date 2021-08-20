import Vue from 'vue'
import Router from 'vue-router'
import Content from '../components/Content'
import Dashboard from '../components/Dashboard'
import Records from '../components/Records'
import Stats from '../components/Stats'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/stats/',
      name: 'Stats',
      component: Stats
    },
    {
      path: '/records/',
      name: 'Records',
      component: Records
    },
  ]
})
