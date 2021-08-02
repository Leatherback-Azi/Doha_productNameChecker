import os, platform, time

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/'
MAIN_FILENAME = os.path.abspath(__file__).replace('\\', '/').split('/')[-1]
OS = platform.system()

CharToDelete = '\\!@#$^=;:\'\",<>`/?()[]{}+*% · ₩,'     # 삭제할 문자들
ReplaceToUnderScore = '　​           /~-'                   # _로 대체할 문자들
CharToBeReplace = '×㎖㎈㎉㎏ℓ㏄㎎'


def clearConsole():
    # 콘솔 클리어. OS별 다른 커맨드
    if OS == 'Windows':
        os.system('cls')
    elif OS == 'Darwin' or OS == 'Linux':
        os.system('clear')


class productNameChecker():
    def __init__(self):
        self.isItActive = True
        while True:
            clearConsole()
            self.old_fileList = list()
            self.changedList = list()
            self.option = input('윈도우 : \'Ctrl + C\' 또는 \'Ctrl + BREAK\'를 이용하여 강제 종료합니다.\nMAC : \'Command + C\'를 이용하여 강제 종료합니다.\n1 - 프로그램의 디렉토리에서 실행. (' + PROJECT_ROOT + ')\n2 - 지정된 디렉토리에서 실행\n3 - 종료\n')
            clearConsole()
            # 1 입력시 실행
            if self.option == '1':
                try:
                    if self.checkDir(PROJECT_ROOT):
                        self.checkName(PROJECT_ROOT)
                        input('\n\n작업이 끝났습니다.\nEnter를 입력하여 계속합니다.')

                except Exception as E:
                    print(str(E) + '\n\n오류가 발생하였습니다.')
                    time.sleep(3)

            # 2 입력시 실행
            elif self.option == '2':
                try:
                    pwd = input('디렉토리를 입력해 주세요')
                    if self.checkDir(pwd):
                        self.checkName(pwd)
                        input('\n\n작업이 끝났습니다.\nEnter를 입력하여 계속합니다')
                except Exception as E:
                    print(str(E) + '\n\n오류가 발생하였습니다.')
                    time.sleep(3)

            # 3 입력시 실행
            elif self.option == '3':
                raise KeyboardInterrupt

            # 잘못된 값 입력 시 실행
            else:
                cnt = 3
                for i in range(3):
                    clearConsole()
                    print('잘못된 입력입니다. ' + str(cnt) + '초 후 선택창으로 돌아갑니다.')
                    cnt -= 1
                    time.sleep(1)
                time.sleep(3)
                self.option = ''

    def __del__(self):
        self.isItActive = False
        print('프로그램을 종료합니다.')
        clearConsole()
        # raise KeyboardInterrupt

    def __repr__(self):
        return self.changedList


    def checkName(self, pwd):
        # 입력된 디렉토리의 모든 파일/폴더를 가져오기
        files = os.listdir(pwd)

        # 폴더는 제외하고 파일만 걸러내는 loop
        for file in files:
            name = os.path.splitext(file)
            name = name[0] + name[1]
            if not os.path.isdir(file):
                if not name == MAIN_FILENAME:
                    self.old_fileList.append(file)
            else:
                pass

        # 파일 이름 가공
        changed = 0
        for productName in self.old_fileList:
            originName = productName
            # 필요 없는 문자 (삭제되어야 할 문자) 발견 시 이름 앞에 !!!!! 붙이기.
            temp = False
            for x in range(len(CharToDelete)):
                if productName.count(CharToDelete[x]) and not temp:
                    productName = '!!!!!' + productName
                    if not temp:
                        temp = True
                        changed += 1
            # 필요한 문자 (ReplaceToUnderScore - 상단에 선언된 String)를 언더바(_)로 수정.
            for x in range(len(ReplaceToUnderScore)):
                if productName.count(ReplaceToUnderScore[x]):
                    productName = productName.replace(ReplaceToUnderScore[x], '_')
                    if not temp:
                        temp = True
                        changed += 1

            replaceChar = 0
            for x in range(len(CharToBeReplace)):
                if productName.count(CharToBeReplace[x]):
                    if not temp:
                        temp = True
                        changed += 1
                        replaceChar += 1

            # 특정 지정 문자를 지정된 값으로 수정. 추후 추가 시 상단의 CharToBeReplace에 추가 요망.
            productName = productName.replace('×', 'X')
            productName = productName.replace('㎖', 'X')
            productName = productName.replace('㎈', 'X')
            productName = productName.replace('㎉', 'X')
            productName = productName.replace('㎏', 'X')
            productName = productName.replace('ℓ', 'X')
            productName = productName.replace('㏄', 'X')
            productName = productName.replace('㎎', 'X')

            if temp:
                self.changedList.append(str(productName))
                os.rename(pwd+originName, pwd+str(productName))
                print('\n' + originName + '\n--> ' + str(productName))
            else:
                self.changedList.append('')

        print('\n\n' + str(len(self.old_fileList)) + '개의 파일 중 ' + str(changed) + '개의 파일이 잘못된것으로 추정됨.')

    # 디렉토리를 올바르게 입력했는지 확인 (실행해도 될 시 True 리턴, 실행하면 안 될 시 False 리턴)
    def checkDir(self, pwd):
        print('선택한 디렉토리 : ' + pwd)
        if not os.path.exists(pwd):
            print('존재하지 않는 경로이거나 해당 폴더의 실행 권한이 없습니다.')
            return False
        if not os.path.isdir(pwd):
            print('잘못된 경로인것 같습니다.')
            return False

        imgFormet = 0
        fileList = os.listdir(pwd)
        for file in fileList:
            if file.find('.jpg'):
                imgFormet += 1
            elif file.find('.png'):
                imgFormet += 1

        if imgFormet <= 10:
            while True:
                ignoreWarn = input('잘못된 디렉토리가 선택 된 것 같습니다. 그래도 진행하시겠습니까? (Y/N)\n')
                if ignoreWarn == 'y' or ignoreWarn == 'Y':
                    return True
                elif ignoreWarn == 'n' or ignoreWarn == 'N':
                    return False
                else:
                    print('잘못된 입력입니다. 다시 선택해 주세요. (Y/N)')

        return True



if __name__ == '__main__':
    try:
        program = productNameChecker()
    except KeyboardInterrupt:
        pass

