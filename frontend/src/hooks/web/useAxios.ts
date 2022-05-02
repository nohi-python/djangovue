import { service } from '@/config/axios'

import { AxiosPromise } from 'axios'

import { config } from '@/config/axios/config'

const { default_headers } = config

export const useAxios = () => {
  const request = <T>(option: AxiosConfig): AxiosPromise<T> => {
    // eslint-disable-next-line prefer-const
    let { url, method, params, data, headersType, responseType } = option

    if (method.toUpperCase() == 'POST') {
      data = {
        header: {
          tranCode: 'QUERY',
          reqFlow: '20220501001',
          reqTime: new Date().getTime(),
        },
        body: data,
      }
    }

    return service({
      url: url,
      method,
      params,
      data,
      responseType: responseType,
      headers: {
        'Content-Type': headersType || default_headers,
      },
    })
  }

  return {
    request,
  }
}
