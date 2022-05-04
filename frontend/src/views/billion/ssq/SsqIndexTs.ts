import axios from 'axios'
import { useAxios } from '@/hooks/web/useAxios'
import { ApiResponse } from '@/api/apitypes'
const { request } = useAxios()

export const apiQuerySsqList = (params: any) => {
  params = {
    header: {
      tranCode: 'QUERY',
      reqFlow: '20220501001',
      reqTime: new Date().getTime(),
    },
    body: params,
  }
  return axios.post('/api/data/ssqList', params)
}

// 同步数据
export const apiRefreshData = () => {
  return axios.post('/api/data/ssqDataRefreshJob')
}

export const apiQuerySsqList2 = (data: any) => {
  return request<ApiResponse>({
    url: '/api/data/ssqList',
    method: 'post',
    data,
  } as AxiosConfig<Recordable>)
}
