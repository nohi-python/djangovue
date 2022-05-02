import axios from 'axios'
import { useAxios } from '@/hooks/web/useAxios'
import { ApiResponse } from '@/api/apitypes'
const { request } = useAxios()

function apiQuerySsqList(params) {
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

export { apiQuerySsqList }

export const apiQuerySsqList2 = (data: any) => {
  return request<ApiResponse>({
    url: '/api/data/ssqList',
    method: 'post',
    data,
  } as AxiosConfig<Recordable>)
}
