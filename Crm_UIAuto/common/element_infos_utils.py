from common.read_excel import ReadExcel
import os


class ElementInfos(object):
    def __init__(self, excel_path, sheet_name):
        self.element = ReadExcel(excel_path, sheet_name).get_excel_data()

    def get_element_info(self):
        element_infos = {}
        for i in range(len(self.element)):
            element_info = {}
            element_info['element_name'] = self.element[i][1]
            element_info['locator_type'] = self.element[i][2]
            element_info['locator_value'] = self.element[i][3]
            element_info['timeout'] = self.element[i][4]
            element_infos[self.element[i][0]] = element_info
        return element_infos

if __name__ == '__main__':
    element_excel_path = os.path.dirname(__file__) + '/../element_infos_datas/element_infos.xlsx'
    e = ElementInfos(element_excel_path, 'login_element').get_element_info()
    print(e)


