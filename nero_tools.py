import random, os, winsound, argparse, inspect
winsound.Beep(500, 300)
os.system("color 0a")
moduleNames = [
            ["random                  ",                            "sys",                              True                                                    ],
            ["argparse                ",                            "sys",                              True                                                    ],
            ["re                      ",                            "sys",                              True                                                    ],
            ["inspect                 ",                            "sys",                              True                                                    ],
            ["faker                   ",                            "additional",                       False,         "Faker    "                              ],
            ["faker.providers         ",                            "additional",                       False,         "job, address, credit_card    "                              ],
            ["wordcloud               ",                            "additional",                       False,         "WordCloud"                              ],
            ["time                    ",                            "sys",                              False,         "sleep"                                  ],
            ["os                      ",                            "sys",                              True                                                    ],
            ["winsound                ",                            "sys",                              True                                                    ],            
            ["pyfiglet                ",                            "additional",                       True                                                    ],
            ["progress.bar            ",                            "additional",                       False,         "ChargingBar"                            ],
            ["vk_api                  ",                            "additional",                       True                                                    ],
            ["pyshorteners            ",                            "additional",                       False,         "*"                                      ],
            ["pyqrcode                ",                            "additional",                       True,          "QRCode"                                 ],
            ["warnings                ",                            "additional",                       True                                                    ],
            ["pystyle                 ",                            "additional",                       True                                                    ]
            ]

menuNames = [
            ["VK tools",                                            "loadMenuVK",                      "VK", True                                                    ],
            ["1 tools",                                            "loadMenu2",                       "VK", False                                                    ],
            ["2 tools",                                            "loadMenu3",                       "VK", False                                                    ],
            ["3 tools",                                            "loadMenu4",                       "VK", False                                                    ],
            ["Other Tools",                                         "loadMenuOT",                      "OT", True                                                    ]
            ]
execNamesVK = [
            ['Add post',                                            'addPost',                          True                                                    ], 
            ['Change status',                                       "status_change",                    True                                                    ], 
            ['Send message',                                        "sendMessage",                      True                                                    ],
            ['Change profile picture',                              "changeProfilePicture",             True                                                    ],
            ['Get list of chats',                                   "getChats",                         True                                                    ],
            ['Get link for access token',                           'getLink',                          True                                                    ] 
            ]
execNamesOT = [
            ['Create short link',                                   'createShortLink',                  "Error"                                                 ],
            ['Create QR-code',                                      'createQR',                         True                                                    ],
            ['Создать облако слов',                                 'createWordCloud',                  True                                                    ],
            ['Создать фейковое имя',                                'createPerson',                     True                                                    ]
]

version = "0.5.2b"
author = "Nakkamurro"
programName = "nero tools"
userFont = "slant"

prefix = "     [" + programName + "] "
input_suffix = " >>> "
class buildMenu(object):
    def buildChosenMenu(self, chosenMenuNumber, execNames):
        try:
            while True:
                print("\n")
                print(pystyle.Center.XCenter(pyfiglet.figlet_format(f" {menuNames[chosenMenuNumber-1][0]}", font = userFont, width=210)))
                print(pystyle.Center.XCenter(f'by {author}\n'))
                sleep(1)
                print(f"{prefix}Choose script:\n")
                ready = 0
                bug = 0
                for i in range(len(execNames)):
                    if execNames[i][2] != False:
                        if execNames[i][2] == 'Error':
                            if i in range(9):
                                bug = bug +1
                                print('\033[31m     >[    ERROR]'+'\033[32m=[ ' + str(int(i+1)) + '] - ' + execNames[i][0] )
                                
                                sleep(0.1)
                            else:
                                bug = bug +1
                                print('\033[31m     >[    ERROR]'+'\033[32m=[' + str(int(i+1)) + '] - ' + execNames[i][0] )
                                
                                sleep(0.1)
                        else:
                            if i in range(9):
                                ready = ready +1
                                print('     >[    READY]=[ ' + str(int(i+1)) + '] - ' + execNames[i][0] )
                                
                                sleep(0.1)
                            else:
                                ready = ready +1
                                print('     >[    READY]=[' + str(int(i+1)) + '] - ' + execNames[i][0] )
                                
                                sleep(0.1)
                    else:
                        if i in range(9):
                            print('     >[NOT READY]=[ ' + str(int(i+1)) + '] - ' + execNames[i][0] )
                            
                            sleep(0.1)
                        else:
                            print('     >[NOT READY]=[' + str(int(i+1)) + '] - ' + execNames[i][0] )
                            
                            sleep(0.1)
                print('\n     To quit input q\exit\quit \n')
                print(f"{prefix}Active " + str(ready + bug) + " methods of " + str(len(execNames)) + f". With bugs loaded {bug} method(s)\n")

                while True:
                    chosenMethod = input(f'{prefix}Chosen method{input_suffix}')
                    if chosenMethod == 'exit' or chosenMethod == 'quit' or chosenMethod == 'Exit' or chosenMethod == "q":
                        localFunction.wipe()
                        Method = None
                        localFunction.loadMenu(Method)
                    elif chosenMethod.isdigit() and 1 <= int(chosenMethod) <= int(len(execNames)):
                        if args.debug:
                            localFunction.debug()
                            localFunction.prToCont()
                            localFunction.wipe()
                            break
                        else:
                            execute = f"execFunction{menuNames[chosenMenuNumber-1][2]}.{str(execNames[int(chosenMethod) - 1][1])}()"
                            localFunction.wipe()
                            exec(execute)
                            localFunction.prToCont()
                            localFunction.wipe()
                            break
                    else:
                        print(f"{prefix}The method number is entered incorrectly! Enter the number corresponding to the function number")    
        except:
            exit(f"\n{prefix}An error occurred in buildMenu.buildChosenMenu() , exiting...")
class localFunction(object):
    def configure(self):
        try:
            functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
            warnings.filterwarnings("ignore")
            os.system(f'title {programName} tokenner v{version} by {author}')
            print()
            print("     Console successfully configured")
            winsound.Beep(700, 1000)
            sleep(2)
        except:
            exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
    def prToCont(self):
        try:
            functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
            sleep(1)
            print()
            os.system('pause')
        except:
            exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
    def wipe(self):
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        os.system('cls' if os.name == 'nt' else 'clear')

    def debug(self):
        try:
            functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
            print(f"{prefix}Debug mode")
            sleep(1)
            print(f"{prefix}Debug mode")
            sleep(1)
            print(f"{prefix}Debug mode")
            sleep(1)
            print(f"{prefix}Exiting...")
        except:
            exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
    def load(self):
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        try:
            bar = ChargingBar('     Please wait, configuring console...                                     ', max = 100)
            for i in range(100):
                bar.next()
                sleep(0.01)
            bar.finish()
        except:
            exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
    def loadModules(self):
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        try:
            bar = ChargingBar('     Loading list of modules...                                              ', max = 100)
            for i in range(100):
                bar.next()
                sleep(0.00001)
            bar.finish()
            bar = ChargingBar('     Loading modules...                                                      ', max = 100)
            for i in range(len(moduleNames)):
                if moduleNames[i][1] == "sys":
                    if moduleNames[i][2] == True:
                        bar = ChargingBar(f'     Full loading system module {moduleNames[i][0]}                     ', max = 100)

                    else:
                        bar = ChargingBar(f'     Partial loading system module {moduleNames[i][0]}                  ', max = 100)

                else:
                    if moduleNames[i][2] == True:
                        bar = ChargingBar(f'     Full loading external module {moduleNames[i][0]}                   ', max = 100)

                    else:
                        bar = ChargingBar(f'     Partial loading external module {moduleNames[i][0]}                ', max = 100)

                for i in range(100):
                    bar.next()
                    sleep(0.00001)
                bar.finish()
            for i in range(len(moduleNames)):    
                if moduleNames[i][2] == False:
                    print(f"     Importing from {moduleNames[i][0]} submodule {moduleNames[i][3]}")
                    sleep(0.1)            
            print("\n     All modules loaded, initialising shell...\n")
            winsound.Beep(700, 300)
            sleep(1)
            localFunction.prToCont()
        except:
            exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
    def loadMenu(self, Method):
            functionName = 'localFunction.'+inspect.currentframe().f_code.co_name 
        # try:
            while True:
                print("\n")
                print(pystyle.Center.XCenter(pyfiglet.figlet_format(programName, font = userFont, width=210)))
                print(pystyle.Center.XCenter(f'by {author}\n'))
                sleep(1)
                print(f"{prefix}Choose menu:\n")
                for i in range(len(menuNames)):
                    if i in range(9):
                        if menuNames[i][3] == True:
                            print('     >[ MENU FOLDER ]=[ ' + str(int(i+1)) + '] - ' + menuNames[i][0] )
                            sleep(0.1)
                    else:
                        if menuNames[i][3] == True:
                            print('     >[ MENU FOLDER ]=[' + str(int(i+1)) + '] - ' + menuNames[i][0] )
                            sleep(0.1)
                print('\n     To quit input q\exit\quit \n')
                try:
                    while True:
                        if Method == None:
                            Method = input(f'{prefix}{input_suffix}')
                            if Method == 'exit' or Method == 'quit' or Method == 'Exit' or Method == "q":
                                exit(f'{prefix}Exiting, goodbye!..')
                            elif Method.isdigit() and 1 <= int(Method) <= int(len(menuNames)):
                                execute = f"localFunction.{str(menuNames[int(Method) - 1][1])}()"
                                localFunction.wipe()
                                exec(execute)
                                localFunction.prToCont()
                                localFunction.wipe()
                                break
                            else:
                                print(f"{prefix}The folder number is entered incorrectly! Enter the number corresponding to the number of the folder with functions")
                        else:
                            try:
                                execute = f"localFunction.{str(menuNames[int(Method) - 1][1])}()"
                                localFunction.wipe()
                                exec(execute)
                                localFunction.prToCont()
                                localFunction.wipe()
                                break
                            except:
                                Method = None
                except:
                    exit(f"\n{prefix}An error occurred in {functionName}, exiting...")
                    
    def loadMenuVK(self):
        global Method
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        try:  
            buildMenu.buildChosenMenu(1, execNamesVK)
        except:
            exit(f"\n{prefix}An unexpected error has occurred, exiting...")
    def loadMenu2(self):
        global Method
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        try:  
            buildMenu.buildChosenMenu(2, execNamesVK)
        except:
            exit(f"\n{prefix}An unexpected error has occurred, exiting...")
    def loadMenuOT(self):
        functionName = 'localFunction.'+inspect.currentframe().f_code.co_name
        global Method
        try:
            buildMenu.buildChosenMenu(5, execNamesOT)
        except:
            exit(f"\n{prefix}An unexpected error has occurred, exiting...")
class execFunctionVK(object):
    def pfglttest(self):
        exampleStr = "Example"
        dir = os.getcwd()
        resultPath = os.path.join(dir, "results.txt")
        fonts = pyfiglet.FigletFont.getFonts()

        file = open(resultPath, 'w')
        for font in fonts:
            fig = pyfiglet.Figlet(font=font)
            result = f"Font: {font}\n{fig.renderText(exampleStr)}\n"
            file.write(result)
        file.close()
    def addPost(self):
        vk = vk_api.VkApi(token = input(f"{prefix}Введите токен пользователя >>>"))
        try:
            vk.method("wall.post", {"message": input(f"{prefix}Введите новый текст поста >>>")})
        except:
            print(f"{prefix}Произошла ошибка при добавлении поста, проверьте токен")
        print(f"{prefix}Пост добавлен успешно!")
    def status_change(self): 
        vk = vk_api.VkApi(token = input(f"{prefix}Введите токен пользователя >>>"))
        try:
            vk.method("status.set", {"text": input(f'{prefix}Введите новый статус :')})
        except:
            print(f"{prefix}Произошла ошибка при смене статуса, проверьте токен")
        print(f'{prefix}Статус сменен успешно!')
    def sendMessage(self):
        vk = vk_api.VkApi(token = input(f"{prefix}Введите токен пользователя >>>"))
        info = input(f'{prefix}Введите айди юзера или чата >>>')
        while True:
            print(f"{prefix}Для выхода напишите exit")
            message = input(f'{prefix}Введите сообщение юзеру >>> ')
            if message != "exit":
                try:
                    vk.method("messages.send", {"peer_id": info, "message": message , "random_id": random.randint(1, 2147483647)})
                except:
                    print(f"{prefix}При отправке сообщения произошла ошибка, проверьте токен")
                print(f'{prefix}Сообщение отправлено успешно') 
            else:
                break      
    def changeProfilePicture(self):
        vk = vk_api.VkApi(token=input(f"{prefix}Введите токен пользователя >>>")) 
        try:
            upload = vk_api.VkUpload(vk)
            photo = upload.photo_profile('avatar.*')
        except:
            print(f"{prefix}Произошла ошибка при смене аватарки, проверьте токен и файл с аватаром")
        print(f"{prefix}Аватар сменен успешно")
    def getChats(self):
        session = vk_api.VkApi(token=input(f"{prefix}Введите токен пользователя >>>"))
        vk = session.get_api()
        n = 0
        user = vk.users.get()
        username = user[0]['first_name'] +  ' ' + user[0]['last_name']
        try:
            print(f"{prefix}Беседы пользователя", username)
            while True:
                n+=1
                peer_ids = 2000000000 + n
                print(vk.messages.getConversationsById(peer_ids = 2000000000 + n, extended = 0)["items"][0]["chat_settings"]["title"], peer_ids)
                info = vk.messages.getConversationsById(peer_ids = 2000000000 + n, extended = 0)["items"][0]["chat_settings"]["title"], peer_ids
        except:
            print(f"{prefix}Все веседы пропарсены, выберите айди нужной беседы")
    # def about(self):
    #     print(f'''
    #                 СПРАВКА ПО ИСПОЛЬЗОВАНИЮ {programName}

    #                 Эта программа предназначена для управления страницей ВКонтакте через токен
    #                 который вы получили заранее.

    #                 Также через эту программу администрируются локальные проекты ST-GURU,
    #                 и небольшие самописные скрипты. Программа регулярно дорабатывается и обновляется.


    #                 Не для публичного пользования
    #                 ''')
    def getLink(self):
        print("                    https://oauth.vk.com/authorize?client_id=6121396&scope=1073737727")
class execFunctionOT(object):
     
    def createShortLink(self):
        # s=pyshorteners.Shortener()
        url = input(f"{prefix}Введите ссылку для сокращения >>>")
        # print(s.tinyurl.short(url))
        # s = pyshorteners.Shortener()
        print(Shortener().tinyurl.short(url))
    def createQR(self):
        url = pyqrcode.create(input(f"{prefix}Введите текст или ссылку для шифрования >>>"))  
        url.svg("qrcode.svg", scale = 8)
    def createWordCloud(self):
        def plot_cloud(wordcloud):
            plt.figure(figsize=(30, 20))
            plt.imshow(wordcloud) 
            plt.axis("off")
            plt.show()

        text = input(f'{prefix}Введите ключевые слова через пробел{input_suffix}')
        wordcloud = WordCloud(width = 2000, height = 1500, random_state=1, background_color='black', margin=20, colormap='Pastel2', collocations=False).generate(text)
        plot_cloud(wordcloud)
        wordcloud.to_file('hp_cloud_simple.png')
    def createPerson(self):
        create = Faker('ru_RU')
        for i in range(3):
            name = create.name()
            age = random.randint(18, 65) + 'Лет'
            job = create.job()
            phone = create.phone_number()
            mail = create.ascii_free_email()
            address = create.address()
            card = create.credit_card_provider() + ' ' + create.credit_card_number()
            cvc_cvv_expires = "CVC/CVV:" + create.credit_card_security_code() + "\nExpires in:" + create.credit_card_expire()
            print(name,age)
            print(job)
            print(phone)
            print(mail)
            print(address)
            print(card)
            print(cvc_cvv_expires)
            print()

buildMenu = buildMenu()
localFunction = localFunction()
execFunctionVK = execFunctionVK()
execFunctionOT = execFunctionOT()

localFunction.wipe()
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fastboot", action="store_true", help="increases speed of boot")
parser.add_argument("-d", "--debug", action="store_true", help="expands output in program")
parser.add_argument("-menu", "--selectmenu", choices = ["1","2"], help="""increases speed of boot WARNING! May cause bugs""")

args = parser.parse_args()
Method = args.selectmenu
try:
    print("\033[32m\n")
    print("     Checking the installed dependencies...")

    for i in range(len(moduleNames)):
        if moduleNames[i][1] == "sys":
            if moduleNames[i][2] == True:#Full import
                output = f"import {moduleNames[i][0]}"
                
                exec(output)
            else:
                output = f"from {moduleNames[i][0]} import {moduleNames[i][3]}"
                
                exec(output)    
        else:#addit lib
            if moduleNames[i][2] == True:#Full import
                output = f"import {moduleNames[i][0]}"
                try:
                    exec(output)
                
                except ImportError:
                    print(f"     [{programName}] Trying to install missing modules: {moduleNames[i][0]}\n")
                    os.system(f'python -m pip install {moduleNames[i][0]}')
                    exec(output)
            else:
                output = f"from {moduleNames[i][0]} import {moduleNames[i][3]}"
                try:
                    exec(output)
                
                except ImportError:
                    print(f"     [{programName}] Trying to install missing modules: {moduleNames[i][0]}\n")
                    os.system(f'python -m pip install {moduleNames[i][0]}')
                    exec(output) 


    sleep(1)
    print("     All dependencies are installed successfully, continue...")
    sleep(1.5)

    if args.fastboot:
        try:
            localFunction.configure()
            localFunction.wipe()
        except:
            print("\n")
            exit('     An error occurred during the system configuration. Update the Libraries or reinstall the system!')
    else:
        try:
            localFunction.load()
            localFunction.configure()
            localFunction.loadModules()
            localFunction.wipe()
        except:
            print("\n")
            exit('     An error occurred during the system configuration. Update the Libraries or reinstall the system!')
    localFunction.loadMenu(Method)
except Exception as error:
    if args.debug:
        print(error)
    exit(f"\n{prefix}An unexpected error has occurred in {functionName}, exiting...")