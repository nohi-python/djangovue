<script setup>
import '../static/css/shiti.css'
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import HelloWorld from './components/HelloWorld.vue'
console.info('App.vue script setup')
</script>

<template>
   <div class="common-layout">
      <el-container>
         <el-aside width="200px">Aside</el-aside>
         <el-container>
            <el-header>Header</el-header>
            <el-main>
               <router-view/>
            </el-main>
            <el-footer>Footer</el-footer>
         </el-container>
      </el-container>
   </div>
</template>
