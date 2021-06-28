import os
import xlrd

element_excel_path = os.path.dirname(__file__) + '/../element_infos_datas/element_infos.xlsx'

class ReadExcel(object):
    #定义参数
    def __init__(self, excel_path, sheet_name):
        #打开路径下的excle文档
        self.workbook = xlrd.open_workbook(excel_path)
        #打开excle文档对应的表名
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    #获取excel的行数
    def get_nrow(self):
        nrow = self.sheet.nrows
        return nrow

    #返回excel的列数
    def get_ncol(self):
        ncol = self.sheet.ncols
        return ncol

    #循环将excle的数据添加到get_excel_datas的列表中
    def get_excel_data(self):
        get_excel_datas = []
        for i in range(1, self.get_nrow()):
            get_excel_data = []
            for j in range(self.get_ncol()):
                #读取excel的第i行，第j列的数据
                data = self.sheet.cell_value(i, j)
                get_excel_data.append(data)
            get_excel_datas.append(get_excel_data)
        return get_excel_datas

if __name__ == '__main__':
    element_data = ReadExcel(element_excel_path, 'login_element').get_excel_data()
    print(element_data)






