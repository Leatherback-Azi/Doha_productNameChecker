import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/'
MAIN_FILENAME = os.path.abspath(__file__).replace('\\', '/').split('/')[-1]

class deleteWrongMark():
    def __init__(self):
        self.pwd = PROJECT_ROOT
        self.old_fileList = list()
        # 입력된 디렉토리의 모든 파일/폴더를 가져오기
        files = os.listdir(self.pwd)

        # 폴더는 제외하고 파일만 걸러내는 loop
        for file in files:
            name = os.path.splitext(file)
            name = name[0] + name[1]
            if not os.path.isdir(file):
                if not name == MAIN_FILENAME:
                    self.old_fileList.append(file)
            else:
                pass

        for productName in self.old_fileList:
            originName = productName
            productName = productName.replace('!', '')
            os.rename(self.pwd + originName, self.pwd + productName)


if __name__ == '__main__':
    try:
        temp = deleteWrongMark()
    except Exception as E:
        print(str(E))
    except KeyboardInterrupt:
        print('KeyboardInterrupt! Exiting...')
