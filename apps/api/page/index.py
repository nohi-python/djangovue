# 分页信息
class PageInfo(object):
    currentPage = 1
    pageSize = 20
    totalPage = 0
    totalRow = 0

    def __init__(self) -> None:
        super().__init__()
