<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Welcome to Your App</h1>
    <el-row justify="center">
      <el-button type="primary" @click="start('sj_01')" round>试卷一</el-button>
      <el-button type="primary" @click="start('sj_02')" round>试卷二</el-button>
    </el-row>
  </div>
</template>

<script>
  // import {watch} from 'vue'
  import {onBeforeRouteLeave, useRoute, useRouter} from "vue-router"

  export default {
    name: "App-Index",
    props: {
      msg: String
    },
    setup() {
      // 获取路由器实例
      const router = useRouter()
      // route是响应式对象,可监控器变化
      const route = useRoute()
      let { id } = route.query
      console.info(id)

      // watch(
      //     () => route.query,
      //     (query) => {
      //       console.log(query)
      //     }
      // )
      // 守卫
      onBeforeRouteLeave((to, from) => {
        console.info(to)
        console.info(from)
        const answer = window.confirm('是否确定要离开')
        if (!answer) {
          return false
        }
      })
      return {
        start: function (sj_no) {
          console.info('goto start page:' + sj_no)
          router.push({
            path:'/shiti',
            query:{
              msg: 'from start',
              sj_no: sj_no
            }
          })

        },
        backToDash() {
          console.log(route.query)
          router.push('/')
        },
      }
    }
  }
</script>
