import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow
from qasync import QEventLoop, asyncSlot
from interface import Ui_takecathome

# Task - disable button clicks

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_takecathome()
        self.ui.setupUi(self)
        
        # Set default to home
        self.ui.stackedWidget.setCurrentIndex(0)
        
        # Set up button connections
        self.ui.back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.back_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.back_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.play.clicked.connect(self.start_game)
        self.ui.settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.credits.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.content_warning.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))

        # Initialize buttons for options
        self.option_clicked = asyncio.Event()
        self.ui.option_1.clicked.connect(lambda: self.option_selected(1))
        self.ui.option_2.clicked.connect(lambda: self.option_selected(2))
        self.ui.option_3.clicked.connect(lambda: self.option_selected(3))
        self.ui.option_4.clicked.connect(lambda: self.option_selected(4))

        # Variables
        self.varHealth = 100
        self.varLevel = 0
        self.ignoreCnt = 0
        self.fastMode = False
        self.disableColorChange = False
        self.disableFlash = False
        self.endingsUnlocked = [False, False, False, False, False, False, False, False, False, False] #if it works, it works.
        self.selected_option = None

    def clear_main(self):
        self.ui.main_text.setText("")

    def clear_options(self):
        self.ui.option_text.setText("")

    # i hope this doesn't make editing ui later on
    async def game_flash(self):
        if not self.disableFlash:
            self.ui.main_text.setStyleSheet("background-color: #261210; border: 2px solid #a15650")
            self.ui.option_text.setStyleSheet("background-color: #261210; border: 2px solid #a15650")
            await asyncio.sleep(0.2)
            self.ui.main_text.setStyleSheet("")
            self.ui.option_text.setStyleSheet("")
            await asyncio.sleep(0.2)
            self.ui.main_text.setStyleSheet("background-color: #261210; border: 2px solid #a15650")
            self.ui.option_text.setStyleSheet("background-color: #261210; border: 2px solid #a15650")
            self.ui.game_page.setStyleSheet("background-color: #261210; border: 2px solid #a15650")
            await asyncio.sleep(0.3)
            self.ui.main_text.setStyleSheet("")
            self.ui.option_text.setStyleSheet("")
            self.ui.game_page.setStyleSheet("")

    async def sleep(self, time, bypass=False):
        if self.fastMode and bypass == False:
            pass
        else:
            await asyncio.sleep(time)


    def battle_mode(self):
        pass


    # Option selection function
    def option_selected(self, option_number):
        self.selected_option = option_number
        print(f"Option {option_number} selected.")
        self.option_clicked.set()  # Signal that an option was selected
        """
        IGNORE--
        Basically a True or False variable but with the help of .set() to chanGE it to either, 
        we can make use of the await func and .wait() to wait till this event has occured. pretty useful.
        """
    def print_main(self, text, append=True):
        if not append:
            self.ui.main_text.setText(text)
        else:
            self.ui.main_text.append(text)
    def print_options(self, text, append=True):
        if not append:
            self.ui.option_text.setText(text)
        else:
            self.ui.option_text.append(text)


    """
    IGNORE--
    Use @asyncSlot when you want to connect an asynchronous function directly to a Qt signal (e.g., a button click).
    This is necessary because Qt expects slots to be synchronous by default, 
    and @asyncSlot allows the function to be used asynchronously in that context.
    """
    @asyncSlot()
    async def start_game(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.fastmode.isChecked():
            self.fastMode = True
        if self.ui.disablecolorchange.isChecked():
            self.disableColorChange = True
        if self.ui.disableflash.isChecked():
            self.disableFlash = True
        await self.game_play_start()

    async def game_play_start(self):
        print("Starting game...")
        #self.ui.main_text.setText("")
        await self.sleep(0.2)
        self.print_main("welcome....", False)
        self.print_main("Seems like your first time playing (...?)")
        await self.sleep(0.7)
        self.print_main("Here main content of the game will appear, as for the second box below this one, it will show the options. Click the option button to select the option. well that's it..")
        self.print_main("< Press any option once done to continue >")
        self.print_options("press any you like (option 1, option 2, option 3, option 4....)")
        
        # Wait for any option button to be clicked
        await self.option_clicked.wait()
        self.print_main(f"\nYou selected the option {self.selected_option} this time...")
        await self.sleep(1.3)
        self.option_clicked.clear()  # Reset the event for future use
        
        # Clear the main text after an option is selected
        self.clear_main()
        self.clear_options()
        # there is no reason to clear these options but iam doing anyways just in case...
        await self.normal_start()

    async def normal_start(self):
        # scene - 1
        print('start 1')
        self.print_main("You find yourself standing in front of a quaint, slightly worn-down animal shelter at the edge of town. You've never been to this area before, but for some reason, it feels oddly familiar, as if you've been here before... at least, something within you says so. You decide to ignore this strange feeling.", False) # why did i turn these False, absolutly no idea but something tells me i should haha
        self.print_main("")
        await self.sleep(1)
        self.print_main("Would you like to enter this shelter?")
        self.print_options("option 1 :- Yes\noption 2 :- No")
        while True:
            await self.option_clicked.wait()
            if self.selected_option > 2:
                self.print_main("\ninvalid option, please select a valid option")
                self.option_clicked.clear()
            else:
                break
        self.option_clicked.clear()
        self.clear_options()
        if self.selected_option == 1:
            await self.go_shelter()
        else:
            pass
    async def go_shelter(self):
        #scene - 2
        self.print_main("Inside the shelter, you discover a cozy, slightly disheveled space filled with the gentle sounds of animals. Soft lighting illuminates a variety of cages and beds, each occupied by curious, hopeful animals awaiting a new home. The air is filled with a comforting blend of pet scents and the faint hum of activity, creating an atmosphere of warmth and anticipation.", False)
        await self.sleep(1)
        self.print_main("\nAmidst them, a strange, fully black cat catches your eye. Its intense, watchful gaze and mysterious presence make it stand out, evoking an inexplicable feeling of unease or familiarity you can’t quite place. The air is filled with a comforting blend of pet scents and the faint hum of activity, but the cat's presence adds an odd twist to the shelter's atmosphere.")
        await self.sleep(2)
        self.print_main("\nShould you adopt this cute little black fur ball?")
        self.print_options("option 1 :- Yes\noption 2 :- No")
        while True:
            await self.option_clicked.wait()
            if self.selected_option > 2:
                self.print_main("\ninvalid option, please select a valid option")
                self.option_clicked.clear()
            else:
                break
        self.option_clicked.clear()
        if self.selected_option == 1:
            pass
        else:
            pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:  # Run the asyncio event loop within the Qt event loop
        loop.run_forever()
