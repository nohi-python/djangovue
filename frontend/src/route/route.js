import { createRouter, createWebHashHistory } from 'vue-router'

// 1. 定义路由组件.
// 也可以从其他文件导入
const Index = () => import('../Index.vue')
const DemoAjax = () => import('../views/demo/Ajax.vue')
const ShitiIndex = () => import('../views/ShitiIndex.vue')
const shiti = () => import('../views/shiti/Start.vue')
const SsqIndex = () => import('../views/billion/ssq/SsqIndex.vue')

// 2. 定义一些路由
// 每个路由都需要映射到一个组件。
// 我们后面再讨论嵌套路由。
const routes = [
  { path: '/', redirect: '/Index' },
  { path: '/Index', component: Index },
  { path: '/DemoAjax', component: DemoAjax },
  { path: '/ShitiIndex', component: ShitiIndex},
  { path: '/shiti', component: shiti },
  { path: '/SsqIndex', component: SsqIndex },
]

const router = createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: createWebHashHistory(),
  routes // `routes: routes` 的缩写
})

router.beforeEach((to, from) => {
  // ...
  console.info('from:' + from.path + 'to:' + to.path)
  // 返回 false 以取消导航
  return true
})

export default router
