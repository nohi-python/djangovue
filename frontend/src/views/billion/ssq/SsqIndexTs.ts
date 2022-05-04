import axios from 'axios'
import { useAxios } from '@/hooks/web/useAxios'
import { ApiResponse } from '@/api/apitypes'
import { config } from '@/config/axios/config'
const { request } = useAxios()

const { base_url } = config

export const PATH_URL = base_url[import.meta.env.VITE_API_BASEPATH]

export const apiQuerySsqList = (params: any) => {
  params = {
    header: {
      tranCode: 'QUERY',
      reqFlow: '20220501001',
      reqTime: new Date().getTime(),
    },
    body: params,
  }
  return axios.post(PATH_URL + '/api/data/ssqList', params)
}

// 同步数据
export const apiRefreshData = () => {
  return axios.post(PATH_URL + '/api/data/ssqDataRefreshJob')
}

export const apiQuerySsqList2 = (data: any) => {
  return request<ApiResponse>({
    url: '/api/data/ssqList',
    method: 'post',
    data,
  } as AxiosConfig<Recordable>)
}
