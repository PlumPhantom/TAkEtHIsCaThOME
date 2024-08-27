# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextBrowser,
    QWidget)

class Ui_takecathome(object):
    def setupUi(self, takecathome):
        if not takecathome.objectName():
            takecathome.setObjectName(u"takecathome")
        takecathome.resize(800, 600)
        takecathome.setStyleSheet(u"QMainWindow {\n"
"	color: green;\n"
"	background-color: black;\n"
"	border: 1px solid purple;\n"
"}\n"
"QWidget {\n"
"    background-color: black;\n"
"    border: 1px solid purple;\n"
"	color: #ff87ff;\n"
"}\n"
"QFrame {\n"
"    background-color: #06020a;\n"
"    border: 1px solid purple;\n"
"	border-radius: 10px;\n"
"}\n"
"QStackedWidget {\n"
"    background-color: #06020a;\n"
"    border: 2px solid purple;\n"
"	color: aqua;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"	border-radius:9px;\n"
"}\n"
"QLabel {\n"
"	border: 0;\n"
"	background-color: None;\n"
"	font-size: 19px\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(takecathome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 801, 601))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #06020a;\n"
"    border: 0.8px solid purple;\n"
"	color: #ff87ff;\n"
"	border-radius: 20px;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.game_lable = QLabel(self.home_page)
        self.game_lable.setObjectName(u"game_lable")
        self.game_lable.setGeometry(QRect(210, 20, 381, 51))
        self.credits = QPushButton(self.home_page)
        self.credits.setObjectName(u"credits")
        self.credits.setGeometry(QRect(321, 281, 161, 41))
        self.play = QPushButton(self.home_page)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(321, 159, 161, 41))
        self.settings = QPushButton(self.home_page)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(321, 220, 161, 41))
        self.achievements = QPushButton(self.home_page)
        self.achievements.setObjectName(u"achievements")
        self.achievements.setGeometry(QRect(321, 342, 161, 41))
        self.content_warning = QPushButton(self.home_page)
        self.content_warning.setObjectName(u"content_warning")
        self.content_warning.setGeometry(QRect(320, 400, 161, 41))
        self.stackedWidget.addWidget(self.home_page)
        self.game_page = QWidget()
        self.game_page.setObjectName(u"game_page")
        self.game_page.setStyleSheet(u"QTextBrowser {\n"
"	border: 1px solid #622678;\n"
"}")
        self.main_text = QTextBrowser(self.game_page)
        self.main_text.setObjectName(u"main_text")
        self.main_text.setGeometry(QRect(180, 30, 421, 271))
        self.option_text = QTextBrowser(self.game_page)
        self.option_text.setObjectName(u"option_text")
        self.option_text.setGeometry(QRect(40, 320, 721, 121))
        self.option_3 = QPushButton(self.game_page)
        self.option_3.setObjectName(u"option_3")
        self.option_3.setGeometry(QRect(420, 450, 101, 41))
        self.option_4 = QPushButton(self.game_page)
        self.option_4.setObjectName(u"option_4")
        self.option_4.setGeometry(QRect(570, 450, 101, 41))
        self.option_1 = QPushButton(self.game_page)
        self.option_1.setObjectName(u"option_1")
        self.option_1.setGeometry(QRect(110, 450, 101, 41))
        self.option_2 = QPushButton(self.game_page)
        self.option_2.setObjectName(u"option_2")
        self.option_2.setGeometry(QRect(260, 450, 101, 41))
        self.stackedWidget.addWidget(self.game_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_lable = QLabel(self.settings_page)
        self.settings_lable.setObjectName(u"settings_lable")
        self.settings_lable.setGeometry(QRect(360, 20, 81, 31))
        self.qqq = QPushButton(self.settings_page)
        self.qqq.setObjectName(u"qqq")
        self.qqq.setGeometry(QRect(360, 450, 80, 41))
        self.qqq.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid darkred;\n"
"	color: red;\n"
"}")
        self.back = QPushButton(self.settings_page)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(330, 520, 151, 23))
        self.disableflash = QCheckBox(self.settings_page)
        self.disableflash.setObjectName(u"disableflash")
        self.disableflash.setGeometry(QRect(321, 235, 161, 21))
        self.fastmode = QCheckBox(self.settings_page)
        self.fastmode.setObjectName(u"fastmode")
        self.fastmode.setGeometry(QRect(321, 146, 161, 21))
        self.disablecolorchange = QCheckBox(self.settings_page)
        self.disablecolorchange.setObjectName(u"disablecolorchange")
        self.disablecolorchange.setGeometry(QRect(321, 324, 161, 21))
        self.stackedWidget.addWidget(self.settings_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.about_textbrowser = QTextBrowser(self.about_page)
        self.about_textbrowser.setObjectName(u"about_textbrowser")
        self.about_textbrowser.setGeometry(QRect(260, 140, 281, 231))
        self.about_lable = QLabel(self.about_page)
        self.about_lable.setObjectName(u"about_lable")
        self.about_lable.setGeometry(QRect(320, 30, 151, 31))
        self.back_2 = QPushButton(self.about_page)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setGeometry(QRect(330, 450, 151, 23))
        self.stackedWidget.addWidget(self.about_page)
        self.achievements_page = QWidget()
        self.achievements_page.setObjectName(u"achievements_page")
        self.stackedWidget.addWidget(self.achievements_page)
        self.content_warn_page = QWidget()
        self.content_warn_page.setObjectName(u"content_warn_page")
        self.content_lable = QLabel(self.content_warn_page)
        self.content_lable.setObjectName(u"content_lable")
        self.content_lable.setGeometry(QRect(320, 30, 191, 31))
        self.content_warn_table = QTextBrowser(self.content_warn_page)
        self.content_warn_table.setObjectName(u"content_warn_table")
        self.content_warn_table.setGeometry(QRect(150, 70, 501, 371))
        self.fun_table = QTextBrowser(self.content_warn_page)
        self.fun_table.setObjectName(u"fun_table")
        self.fun_table.setGeometry(QRect(260, 450, 256, 91))
        self.back_3 = QPushButton(self.content_warn_page)
        self.back_3.setObjectName(u"back_3")
        self.back_3.setGeometry(QRect(310, 560, 151, 23))
        self.stackedWidget.addWidget(self.content_warn_page)
        takecathome.setCentralWidget(self.centralwidget)

        self.retranslateUi(takecathome)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(takecathome)
    # setupUi

    def retranslateUi(self, takecathome):
        takecathome.setWindowTitle(QCoreApplication.translate("takecathome", u"MainWindow", None))
        self.game_lable.setText(QCoreApplication.translate("takecathome", u"Take this absolutely adorable cute cat home!", None))
        self.credits.setText(QCoreApplication.translate("takecathome", u"About", None))
        self.play.setText(QCoreApplication.translate("takecathome", u"Play!", None))
        self.settings.setText(QCoreApplication.translate("takecathome", u"Settings", None))
        self.achievements.setText(QCoreApplication.translate("takecathome", u"Achievements", None))
        self.content_warning.setText(QCoreApplication.translate("takecathome", u"Content warnings", None))
        self.main_text.setHtml(QCoreApplication.translate("takecathome", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.option_text.setHtml(QCoreApplication.translate("takecathome", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.option_3.setText(QCoreApplication.translate("takecathome", u"Option 3", None))
        self.option_4.setText(QCoreApplication.translate("takecathome", u"Option 4", None))
        self.option_1.setText(QCoreApplication.translate("takecathome", u"Option 1", None))
        self.option_2.setText(QCoreApplication.translate("takecathome", u"Option 2", None))
        self.settings_lable.setText(QCoreApplication.translate("takecathome", u"Settings", None))
        self.qqq.setText(QCoreApplication.translate("takecathome", u"???", None))
        self.back.setText(QCoreApplication.translate("takecathome", u"return to home page..", None))
        self.disableflash.setText(QCoreApplication.translate("takecathome", u"disable flashing screen", None))
        self.fastmode.setText(QCoreApplication.translate("takecathome", u"fastmode", None))
        self.disablecolorchange.setText(QCoreApplication.translate("takecathome", u"Don't change ui color", None))
        self.about_textbrowser.setHtml(QCoreApplication.translate("takecathome", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A <span style=\" font-weight:700;\">cute</span> game about adopting a cat.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Trust me when I say its just a <span style=\" font-weight:700;\">normal</span> cat ;&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">And most importantly, really adorable as well!</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536;\">-GloomyCatto</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This game was made because I\u2019m really, really, really in love with cats!</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />Everything, including the story"
                        ", coding, and more, was done by <span style=\" font-weight:700;\">GloomyCatto</span>.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Thanks for playing!</span></p></body></html>", None))
        self.about_lable.setText(QCoreApplication.translate("takecathome", u"About this game", None))
        self.back_2.setText(QCoreApplication.translate("takecathome", u"return to home page..", None))
        self.content_lable.setText(QCoreApplication.translate("takecathome", u"Content Warning :>", None))
        self.content_warn_table.setHtml(QCoreApplication.translate("takecathome", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Abuse / Abusive Relationship(s)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Agoraphobia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amnesia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\">Animal Abuse</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animal Death</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Animals/Monsters Eating Humans</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Anxiety / Social Anxiety</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Body Horror</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Body Injury</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cannibalism</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\">Child Abuse (Minor Mention/Hint Of)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cosmic Horror</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dead Bodies &amp; Body Parts</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Death / Dying</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decapitation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Depression</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dissociation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\">Doll Animation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Emotional Abuse</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Entrapment</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hallucinations</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Heart Attack</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Intrusive Thoughts</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Isolation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Kidnapping / Abduction</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Loss of Vision</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Manipulation / Gaslighting</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mental Illness</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mind Control</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Murder</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paranoia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">Poison / Venom</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Psychological Horror</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Scary / Disturbing Images &amp; Messages</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Scopophobia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Self-harm</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Stalking</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Suicide / Suicidal Ideation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">Tense Situations / Gameplay</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thalassophobia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Violence</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vomiting</p></body></html>", None))
        self.fun_table.setHtml(QCoreApplication.translate("takecathome", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Trust me, and feel free to ignore these.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">:&gt;&gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">totally not something you have to worry about"
                        ".</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">just relax and enjoy the game!</p></body></html>", None))
        self.back_3.setText(QCoreApplication.translate("takecathome", u"return to home page..", None))
    # retranslateUi

