import axios from 'axios'
import { useAxios } from '@/hooks/web/useAxios'
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

export const apiQuerySsqList2 = (data: object) => {
  return request<{
    total: number
    list: UserType[]
  }>({
    url: '/api/data/ssqList',
    method: 'POST',
    data,
  } as AxiosConfig<Recordable>)
}
