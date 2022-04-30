import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import routes from './route/route'
import test from './store/test'

// 试卷、试题
// const shijuan = require('../static/data/shijuan.json')
// const shiti = require('../static/data/shiti.json')
import shijuan from '../static/data/shijuan.json'
import shiti from '../static/data/shiti.json'

const app = createApp(App)
app.use(ElementPlus)

app.use(routes)
app.use(test)
app.mount('#app')

const getShijuan = new Promise((resolve, reject) => {
  unuser(reject)
  // createApp(App).config.globalProperties.$shijuan = shijuan
  app.config.globalProperties.$shijuan = shijuan
  resolve()
})
const getShiti = new Promise((resolve, reject) => {
  unuser(reject)
  // createApp(App).config.globalProperties.$shiti = shiti
  app.config.globalProperties.$shiti = shiti
  resolve()
})
unuser(getShijuan)
unuser(getShiti)

function unuser (obj) {
  if (typeof obj == 'undefined') {
    console.info('undifine')
  }
}
