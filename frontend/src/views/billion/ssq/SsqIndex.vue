<template>
  <el-radio-group v-model="labelPosition">
    <el-radio-button label="left">Left</el-radio-button>
    <el-radio-button label="right">Right</el-radio-button>
    <el-radio-button label="top">Top</el-radio-button>
  </el-radio-group>
  <div style="margin: 20px"></div>
  <el-form
    :inline="true"
    :label-position="labelPosition"
    label-width="100px"
    :model="formLabelAlign"
    class="demo-form-inline"
  >
    <el-form-item label="期次">
      <el-col :span="11">
        <el-input v-model="formLabelAlign.qiCiStart" />
      </el-col>
      <el-col class="text-center" :span="1" style="margin: 0 0.5rem">-</el-col>
      <el-col :span="10">
        <el-input v-model="formLabelAlign.qiCiEnd" />
      </el-col>
    </el-form-item>
    <el-form-item label="日期">
      <el-col :span="10">
        <el-date-picker
          v-model="formLabelAlign.dataStart"
          type="date"
          placeholder="开始日期"
          style="width: 97%"
        />
      </el-col>
      <el-col class="text-center" :span="1" style="margin: 0 0.5rem">-</el-col>
      <el-col :span="10">
        <el-date-picker
          type="date"
          v-model="formLabelAlign.dataEnd"
          placeholder="结束日期"
          style="width: 97%"
        />
      </el-col>
    </el-form-item>
    <el-form-item>
      <el-checkbox-group v-model="lastQiCi">
        <el-checkbox-button label="ten" @click="lastQiCiClick('tent')"
          >最近10期</el-checkbox-button
        >
        <el-checkbox-button label="twenty" @click="lastQiCiClick('twenty')"
          >最近20期</el-checkbox-button
        >
        <el-checkbox-button label="hundred" @click="lastQiCiClick('houdred')"
          >最近100期</el-checkbox-button
        >
      </el-checkbox-group>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">查询</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>

  <el-table
    :data="ssqList"
    style="width: 100%"
    :header-cell-style="{ textAlign: 'center' }"
    :cell-style="{ textAlign: 'center' }"
  >
    <el-table-column prop="fields.qiCi" label="期次" width="120px" />
    <el-table-column prop="fields.kaiJiangRiQi" label="日期" width="140px" />
    <el-table-column label="开奖号码">
      <el-table-column prop="fields.hongYi" label="红1" width="80px" />
      <el-table-column prop="fields.hongEr" label="红2" width="80px" />
      <el-table-column prop="fields.hongSan" label="红3" width="80px" />
      <el-table-column prop="fields.hongSi" label="红4" width="80px" />
      <el-table-column prop="fields.hongWu" label="红5" width="80px" />
      <el-table-column prop="fields.hongLiu" label="红6" width="80px" />
      <el-table-column prop="fields.langQiu" label="蓝" width="80px" />
    </el-table-column>
    <el-table-column label="一等奖">
      <el-table-column prop="fields.yiDengJiangZhuShu" label="注数" />
      <el-table-column prop="fields.yiDengJiangJiangJin" label="金额" />
    </el-table-column>
    <el-table-column prop="name" label="二等奖">
      <el-table-column prop="fields.erDengJiangZhuShu" label="注数" />
      <el-table-column prop="fields.erDengJiangJiangJin" label="金额" />
    </el-table-column>
  </el-table>
  <div class="demo-pagination-block">
    <div class="demonstration"></div>
    <el-pagination
      v-model:currentPage="pageInfo.currentPage"
      v-model:page-size="pageInfo.pageSize"
      :page-sizes="[10, 20, 50, 100]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="pageInfo.totalRow"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, watch } from 'vue'
import { apiQuerySsqList2 } from './SsqIndexTs'

let ssqList = ref([])
const labelPosition = ref('right')
const lastQiCi = ref([])
let pageInfo = ref({
  currentPage: 1,
  pageSize: 20,
  totalPage: 0,
  totalRow: 0,
})

const formLabelAlign = reactive({
  qiCiStart: '',
  qiCiEnd: '',
  dataStart: '',
  dataEnd: '',
  lastQiCi: '',
})

// 选择值变
function lastQiCiClick(val: string) {
  console.info('val:' + val + ',curvalue:' + lastQiCi.value)
  lastQiCi.value.forEach((item) => {
    if (item != val) {
      lastQiCi.value.pop(item)
    }
  })
}

// 事件监听
watch(lastQiCi, (newValue, oldValue) => {
  // oldValue 已经从click事件中删除，这里永远为''
  console.info('lastQiCi.value:' + newValue + ', from:' + oldValue)
  if (newValue != '') {
    pageInfo.value.currentPage = 1
    formLabelAlign.qiCiStart = ''
    formLabelAlign.qiCiEnd = ''
    formLabelAlign.dataStart = ''
    formLabelAlign.dataEnd = ''
    formLabelAlign.lastQiCi = newValue[0]
    querySsqList()
  }
})

// 查询
function onSubmit() {
  console.log('submit!')
  // 重新查询后轩当前页为1
  pageInfo.value.currentPage = 1
  querySsqList()
}

// 页数变更
function handleSizeChange(): void {
  console.info('每页页数变更')
  querySsqList()
}

// 跳转页
function handleCurrentChange() {
  console.info('中转至page:' + pageInfo.value.currentPage)
  querySsqList()
}

async function querySsqList() {
  const param = {
    pageInfo: pageInfo.value,
    formParm: formLabelAlign,
  }
  console.info('请求：' + JSON.stringify(param))

  // 自定义方式查询
  // apiQuerySsqList(param)
  //   .then((response) => {
  //     console.info('response1:' + response)
  //   })
  //   .catch(() => {})
  //   .finally(() => console.info('finally....'))

  apiQuerySsqList2(param)
    .then((response) => {
      // console.info('response2:' + JSON.stringify(response))
      ssqList.value = response.data.body.data
      pageInfo.value = response.data.body.pageInfo
      console.info(ssqList)
      console.info(pageInfo)
    })
    .catch(() => {})
    .finally(() => console.info('finally....'))
}

console.info('env:' + import.meta.env.VITE_API_BASEPATH)
</script>
<script lang="ts">
export default {}
</script>
