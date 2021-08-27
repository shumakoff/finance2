import Vue from 'vue'
import axios from 'axios';
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'
import { faPlusCircle } from '@fortawesome/free-solid-svg-icons'
import { faChartArea } from '@fortawesome/free-solid-svg-icons'
import { faBars } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Notifications from 'vue-notification'
import vueNumeralFilterInstaller from 'vue-numeral-filter';
import numeral from 'numeral'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import '../static/css/sb-admin-2.css';

if (process.env.NODE_ENV != "development") {
    var baseURL = "/api/v1/" } else { var baseURL = 'http://localhost:8000/api/v1/' }
axios.defaults.baseURL = baseURL // the prefix of the URL

library.add(faSearch)
library.add(faArrowLeft)
library.add(faArrowRight)
library.add(faPlusCircle)
library.add(faChartArea)
library.add(faBars)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(Notifications)
Vue.use(vueNumeralFilterInstaller)//, { locale: 'ru' });
Vue.use(VueCookies)

Vue.prototype.$nestObjects = function(objects){
  var unwanted_kids = [];
  for (var idx = 0; idx < objects.length; idx++) {
    for (var idx2 = 0; idx2 < objects.length; idx2++) {
      if (objects[idx].parent === objects[idx2].id) {
        if (objects[idx2].children == undefined) {
          objects[idx2].children = [];
        }
        objects[idx2].children.push(objects[idx]);
        unwanted_kids.push(idx+1);
      }
    }
  }
  for (var kid of unwanted_kids) {
    objects[kid-1] = null;
  }
  var result = []
  for (var obj of objects) {
    if (obj) {
      result.push(obj);
    }
  }
  return (result);
}

new Vue({
  el: '#wrapper',
  router,
  render: h => h(App)
})

axios.defaults.headers.common['X-CSRFToken'] = Vue.$cookies.get('csrftoken');

