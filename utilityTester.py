
from utils import updater
from utils.menu import Menu
from utils.logger import Logger
import testFunctions
log = Logger(r"./UtilityTester",4)

log.hd("Hard Debug")
log.d("Debug")
log.i("info")
log.w("warning")
log.e("error")
upd = updater.Updater()

file_menu = Menu("File Menu",[
    ["Test Lettura File",testFunctions.test_read_file],
    ["Test Scrittura File",testFunctions.test_write_file]
])


main_menu = Menu("Main Menu",[
    ["Menu File",file_menu.run],
    ["Check Update",upd.check_updates],
])
main_menu.debug = True
main_menu.run()
