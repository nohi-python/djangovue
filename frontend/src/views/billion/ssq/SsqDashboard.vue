<template>
  <h1>Dashboard</h1>
  <el-button type="primary" @click="refreshData">同步数据</el-button>
  <el-form
    :inline="true"
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

  <ElRow :gutter="20" justify="space-between">
    <ElCol :span="24">
      <ElCard shadow="hover" class="mb-20px">
        <ElSkeleton :loading="loading" animated :rows="4">
          <div ref="test" style="width: 100%; height: 700px"></div>
        </ElSkeleton>
      </ElCard>
    </ElCol>
  </ElRow>
</template>

<script lang="ts" setup>
import { ElRow, ElCol, ElCard, ElSkeleton } from 'element-plus'
import { onMounted, reactive, ref, watch } from 'vue'
import * as echarts from 'echarts'
import {
  apiQuerySsqList2,
  apiRefreshData,
} from '@/views/billion/ssq/SsqIndexTs'

const loading = ref(false)
let ssqList = ref([])
const lastQiCi = ref(['ten'])
let pageInfo = ref({
  currentPage: 1,
  pageSize: 100,
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

// 同步数据开始
async function refreshData() {
  console.log('同步数据开始!')
  const data = await apiRefreshData()
  console.info(data)
  console.log('同步数据结束!')
}

// 查询
function onSubmit() {
  console.log('submit!')
  // 重新查询后轩当前页为1
  pageInfo.value.currentPage = 1
  querySsqList()
}

let xAxisData = []
let seriesData1 = []
let seriesData2 = []
let seriesData3 = []
let seriesData4 = []
let seriesData5 = []
let seriesData6 = []
let seriesData7 = []

let test = ref(null) // 获取div元素，这里与vue2.x的写法不一样了
let myChart = null

function line() {
  console.info('line')
  const option = {
    title: {
      text: '历史趋势！',
      textStyle: {
        color: 'red',
        fontStyle: 'oblique',
      },
    },
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['红一', '红二', '红三', '红四', '红五', '红六', '蓝球'],
    },
    grid: {
      left: '3%',
      right: '4%',
      // bottom: '3%',
      containLabel: true,
    },
    toolbox: {
      feature: {
        // saveAsImage: {},
      },
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      axisLabel: {
        rotate: -45,
      },
      data: xAxisData,
    },
    yAxis: {
      type: 'value',
      axisTick: {
        show: false,
      },
      data: [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
      ],
    },
    series: [
      {
        name: '红一',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData1,
      },
      {
        name: '红二',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData2,
      },
      {
        name: '红三',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData3,
      },
      {
        name: '红四',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData4,
      },
      {
        name: '红五',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData5,
      },
      {
        name: '红六',
        type: 'line',
        itemStyle: {
          color: '#fc8452',
        },
        data: seriesData6,
      },
      {
        name: '蓝球',
        type: 'line',
        itemStyle: {
          color: 'blue',
        },
        data: seriesData7,
      },
    ],
  }
  console.info(JSON.stringify(option))
  myChart.setOption(option)
}
async function querySsqList() {
  const param = {
    pageInfo: pageInfo.value,
    formParm: formLabelAlign,
  }
  console.info('请求：' + JSON.stringify(param))
  apiQuerySsqList2(param)
    .then((response) => {
      // console.info('response2:' + JSON.stringify(response))
      ssqList.value = response.data.body.data
      initEcharLine()
    })
    .catch(() => {})
    .finally(() => console.info('finally....'))
}

function initEcharLine() {
  console.info('initEcharLine.....')
  xAxisData = []
  seriesData1 = []
  seriesData2 = []
  seriesData3 = []
  seriesData4 = []
  seriesData5 = []
  seriesData6 = []
  seriesData7 = []
  console.info('ssqList.value.length:' + ssqList.value.length)
  for (let i = ssqList.value.length - 1; i > 0; i--) {
    const item = ssqList.value[i].fields
    xAxisData.push(item.qiCi)
    seriesData1.push(item.hongYi)
    seriesData2.push(item.hongEr)
    seriesData3.push(item.hongSan)
    seriesData4.push(item.hongSi)
    seriesData5.push(item.hongWu)
    seriesData6.push(item.hongLiu)
    seriesData7.push(item.langQiu)
  }
  line()
}

onMounted(() => {
  console.info('onMounted start')
  myChart = echarts.init(test.value)
  formLabelAlign.lastQiCi = lastQiCi.value[0]
  querySsqList()
  console.info('onMounted end')
})
</script>
