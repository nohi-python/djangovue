export type ApiResponseHeader = {
  tranCode: string
  reqFlow: string
  reqTime: number
  respTime: number
  respCode: string
  respMsg: string
}

export type ApiResponse = {
  header: ApiResponseHeader
  body: any
}
