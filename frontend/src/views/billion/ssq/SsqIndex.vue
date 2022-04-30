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
      <el-radio-group v-model="lastQiCi">
        <el-radio-button label="ten">最近10期</el-radio-button>
        <el-radio-button label="twenty">最近20期</el-radio-button>
        <el-radio-button label="hundred">最近100期</el-radio-button>
      </el-radio-group>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">查询</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>

  <el-table :data="ssqList" style="width: 100%">
    <el-table-column prop="qiCi" label="期次" />
    <el-table-column prop="kaiJiangRiQi" label="日期" width="110px" />
    <el-table-column label="开奖号码">
      <el-table-column prop="name" label="红1" />
      <el-table-column prop="name" label="红2" />
      <el-table-column prop="name" label="红3" />
      <el-table-column prop="name" label="红4" />
      <el-table-column prop="name" label="红5" />
      <el-table-column prop="name" label="红6" />
      <el-table-column prop="name" label="蓝" />
    </el-table-column>
    <el-table-column prop="name" label="一等奖">
      <el-table-column prop="name" label="注数" />
      <el-table-column prop="name" label="金额" />
    </el-table-column>
    <el-table-column prop="name" label="二等奖">
      <el-table-column prop="name" label="注数" />
      <el-table-column prop="name" label="金额" />
    </el-table-column>
    <el-table-column prop="name" label="三等奖">
      <el-table-column prop="name" label="注数" />
      <el-table-column prop="name" label="金额" />
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
import { reactive, ref } from 'vue'
import { getName } from '@/api/requests/index'

const ssqList = [
  {
    kaiJiangRiQi: '2016-05-03',
    qiCi: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]

const labelPosition = ref('right')
const lastQiCi = ref('ten')
const pageInfo = ref({
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
  name: '',
  region: '',
  type: '',
})

// 查询
function onSubmit() {
  console.log('submit!')
  getName()
}

// 页数变更
function handleSizeChange() {}

// 跳转页
function handleCurrentChange() {}
</script>
