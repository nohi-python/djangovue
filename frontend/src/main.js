import { createApp } from 'vue'
import App from './App.vue'
import routes from './route/route'
import test from './store/test'

const app = createApp(App)
app.use(routes)
app.use(test)
app.mount('#app')
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true
  },
  extends: [
    'plugin:vue/essential',
    'standard'
  ],
  parserOptions: {
    ecmaVersion: 13,
    sourceType: 'module'
  },
  plugins: [
    'vue'
  ],
  rules: {}
}
