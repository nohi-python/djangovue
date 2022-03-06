<script setup>
console.info('Index.vue script setup...')
</script>
<script>
console.info('Index.vue script')
export default {
  data: function () {
    return {
      replace: true
    }
  }
}
</script>

<template>
  <img alt="Vue logo" src="./assets/logo.png"/>
  <p>
    <!--使用 router-link 组件进行导航 -->
    <!--通过传递 `to` 来指定链接 -->
    <!--`<router-link>` 将呈现一个带有正确 `href` 属性的 `<a>` 标签-->
    <router-link to="/">Go to Index</router-link>&nbsp;&nbsp;
  </p>
  <p>
    <router-link to="/DemoAjax">DemoAjax</router-link>&nbsp;&nbsp;
  </p>
</template>

<style>

</style>
