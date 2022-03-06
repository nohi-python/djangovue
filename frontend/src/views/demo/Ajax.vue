<script>
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { ref, watch } from 'vue'
import axios from 'axios'

export default {
  setup () {
    const route = useRoute()
    const userData = ref()

    // 当参数更改时获取用户信息
    watch(
      () => route.params,
      async newParams => {
        console.info('route.params:' + JSON.stringify(route.params))
        userData.value = route.params // await fetchUser(newParams.id)
      }
    )

    // 与 beforeRouteLeave 相同，无法访问 `this`
    onBeforeRouteUpdate(async (to, from) => {
      // 仅当 id 更改时才获取用户，例如仅 query 或 hash 值已更改
      if (to.params.id !== from.params.id) {
        console.info('onBeforeRouteUpdate route.params:' + JSON.stringify(route.params))
      }
    })
  },
  data () {
    return {
      questionJson: [],
      questionList: []
    }
  },
  computed: {
    username () {
      // 我们很快就会看到 `params` 是什么
      return this.$route.query.username
    },
    userid () {
      return this.$route.params.id
    }
  },
  methods: {
    goToHome () {
      this.$router.push('/')
    },
    refresh () {
      console.info('Ajax...refresh')
      axios
        .get('http://127.0.0.1:8000/polls/questionJsonTwo')
        .then(response => (this.questionJson = response.data))
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
    },
    refreshDbData () {
      console.info('Ajax...refreshDbData')
      axios
        .get('http://127.0.0.1:8000/polls/questionList')
        .then(response => (this.questionList = response.data))
        .catch(function (error) { // 请求失败处理
          console.log(error)
        })
    }
  },
  created () {
    this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        // 对路由变化做出响应...
        console.info('toParams:' + JSON.stringify(toParams) + ',previousParams:' + JSON.stringify(previousParams))
      }
    )
  },
  async beforeRouteUpdate (to, from) {
    // 对路由变化做出响应...
    console.info('to.params.id:' + to.params.id)
  },
  beforeRouteLeave (to, from) {
    const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
    if (!answer) return false
  }
}
</script>
<template>
  <h2>userid:{{ userid }},username:{{ username }}</h2>
  <button @click="goToHome">GO HOME</button>
  <button @click="refresh">Refresh</button>
  <button @click="refreshDbData">RefreshDbData</button>
  <div>
    <h4>questionJson</h4>
    <table>
      <tr v-for="(item, index) in questionJson" :key="item.id">
        <td>{{ index }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.age }}</td>
        <td>{{ item.addr }}</td>
      </tr>
    </table>
     <h4>questionList</h4>
    <table>
      <tr v-for="(item, index) in questionList" :key="item.id">
        <td>{{ index }}</td>
        <td>{{ item.fields.question_text }}</td>
        <td>{{ item.fields.pub_date }}</td>
      </tr>
    </table>
  </div>

</template>

<style>

</style>
