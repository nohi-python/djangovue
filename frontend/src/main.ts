import { createApp } from 'vue'
// 引入element-plus
import { setupElementPlus } from '@/plugins/elementPlus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import routes from './route/route'
// 引入状态管理
import { setupStore } from '@/store'
// 路由
// import { setupRouter } from './router'
// 试卷、试题
// const shijuan = require('../static/data/shijuan.json')
// const shiti = require('../static/data/shiti.json')
import shijuan from '@/assets/static/data/shijuan.json'
import shiti from '@/assets/static/data/shiti.json'

const setupAll = async () => {
  const app = createApp(App)

  setupElementPlus(app)
  setupStore(app)
  app.use(routes)
  app.mount('#app')

  // 加载试卷
  const getShijuan = new Promise<void>((resolve, reject) => {
    unuser(reject)
    // createApp(App).config.globalProperties.$shijuan = shijuan
    app.config.globalProperties.$shijuan = shijuan
    resolve()
  })
  const getShiti = new Promise<void>((resolve, reject) => {
    unuser(reject)
    // createApp(App).config.globalProperties.$shiti = shiti
    app.config.globalProperties.$shiti = shiti
    resolve()
  })
  unuser(getShijuan)
  unuser(getShiti)
}

setupAll()

function unuser(obj) {
  if (typeof obj == 'undefined') {
    console.info('undifine')
  }
}
