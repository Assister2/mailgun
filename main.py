# This is a program to send emails automatically with user interface 
# Author: Developer and Enfineer Gad Badr @ https://devgadbadr.github.io/personal-website/


import email
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QFileDialog
from mainUI import Ui_MainWindow
from autoui import Ui_Dialog
import openpyxl
from mailgunconf import Ui_MG
from emailssends import EmailSender
import time
from PyQt5.QtCore import QTimer
    
class MainWindow(Ui_MainWindow):
    
    def mainView(self,window):
        
        super().setupUi(window)
        self.myedit()
        self.readNumbers()
        self.readRecipients()
        self.setsender()
        self.readTails()
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_press)
        
        
        if not self.last:
            self.nextEmaills.hide()
            self.PrevEmails.hide()
            
            pass
        else:
            self.automModeCheck()
            with open('.\\Resources\\lastIndex.txt','r') as n:
                i = n.read()
            n.close()
            
            if int(i)>1:
                for m in range(1,int(i)):
                    self.nextEmaills.click()
                    self.NextnumberButton.click()
                    
            self.checkFinished()
            
            if self.finished:
                self.activeModeLabel.setText('Finished')
                self.StopAutomaticButton.hide()
            
            
    

    def myedit(self):
        
        self.row = 0
        self.varyNum = 0
        self.varyRecp = 0
        
        # Initialize
        with open('.\\Resources\\lastNumbersFile.txt','r') as n:
            p = n.read()
        n.close()
        if len(p)==0:
            self.last = False
            pass
        else:
            self.last = True
            self.readbrowsedFile(p)

        self.recipient1box.textChanged.connect(self.change)
        self.recipient2box.textChanged.connect(self.change)
        self.recipient3box.textChanged.connect(self.change)
        self.currentNumberBox.textChanged.connect(self.change)
        self.emailToBox.textChanged.connect(self.change)
        
        # Buttons 
        self.browseButton.clicked.connect(self.browseFile)
        self.prepareEmailButton.clicked.connect(self.prepareEmail)
        self.SendEmailBox.clicked.connect(self.sendEmail)
        self.StopAutomaticButton.clicked.connect(self.stopAutoMode)
        self.closeButton.clicked.connect(self.closeprogram)
        self.NextnumberButton.clicked.connect(self.nextnumber)
        self.previouNumberButton.clicked.connect(self.previousnumber)
        self.nextEmaills.clicked.connect(self.nextemails)
        self.PrevEmails.clicked.connect(self.prevemails)
        self.rece1tail.textChanged.connect(self.writeTails)
        self.rece2tail.textChanged.connect(self.writeTails)
        self.rece3tail.textChanged.connect(self.writeTails)
         
        # Bar Actions
        self.actionAutomatic_Sending.triggered.connect(self.automMode)
        self.actionReset_Interface.triggered.connect(self.resetinterface)
        self.actionOpen_Numbers_Shhet.triggered.connect(self.opennumbersSheet)
        self.actionOpen_Recipients_File.triggered.connect(self.openrecipientsFile)
        self.actionOpen_the_Log_File.triggered.connect(self.openLogFile)
        self.actionUpdate_Numbers.triggered.connect(self.updatenumbers)
        self.actionCurrent_Numbers_List.triggered.connect(self.openNubers)
        self.actionMail_Gun_Confiduration.triggered.connect(self.mailgunConf)
        self.actionEdit_Email.triggered.connect(self.openemail)
        
        # Hide
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        self.StopAutomaticButton.hide()
        self.activeModeLabel.hide()
        self.SendEmailBox.setDisabled(True)
    
    def checkFinished(self):
        
        currentIndex=int(self.IndexNumber.text())
        numberOfReces = len(self.recipients)
        self.finished=False
        print(currentIndex)
        print(numberOfReces)
        
        if currentIndex==numberOfReces:
            self.finished = True
        
        
    def change(self):
        self.emailTextBox.clear()
        self.SendEmailBox.setDisabled(True)
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        
    def nextemails(self):
        
        if self.emailrow<len(self.recipients)-1:
            row = self.emailrow
            
            self.IndexNumber.setText(str((row+1)+1))
            
            nexemail1 = self.recipients[row+1]
            try:
                nexemail2 = self.recipients[row+1]
            except IndexError:
                nexemail2 = ''
            try:
                nexemail3 = self.recipients[row+1]
            except IndexError:
                nexemail3 = ''
            
            self.recipient1box.setText(nexemail1)
            self.recipient2box.setText(nexemail2)
            self.recipient3box.setText(nexemail3)
            self.emailrow+=1
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
           
    def prevemails(self):
        
        if self.emailrow>=1:
            row = self.emailrow
            self.IndexNumber.setText(str((row+1)-1))
            nexemail1 = self.recipients[row-1]
            nexemail2 = self.recipients[row-1]
            nexemail3 = self.recipients[row-1]
            
            self.recipient1box.setText(nexemail1)
            self.recipient2box.setText(nexemail2)
            self.recipient3box.setText(nexemail3)
            self.emailrow-=1
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
        
    def mailgunConf(self):
        
        class nativeMG(Ui_MG):
            
            def __init__(self) -> None:
                super().__init__()

            def saveMG(self):
                
                domain = y.lineEdit.text()
                api_key= y.lineEdit_2.text()
                sender_name = y.lineEdit_3.text()
                sender_email = y.lineEdit_4.text()
                
                # MailGun Configuration
                with open('.\\Resources\\mailGun.txt','w') as b:
                    b.write(domain+'\n')
                    b.write(api_key+'\n')
                    b.write(sender_name+'\n')
                    b.write(sender_email+'\n')
                b.close()
                y.label_5.show()
                
            def closeMG(self):
                w.close()
            
                
        # MailGun Configuration
        with open('.\\Resources\\mailGun.txt','r') as b:
            n = b.readlines()
            data=[]
            for i in n:
                f = i.replace('\n','')   
                data.append(f)
        b.close()
        
        y = nativeMG()
        w = QtWidgets.QDialog()
        w.setWindowIcon(QtGui.QIcon('icon.png'))
        y.setupUi(w)
        y.label_5.hide()
        y.lineEdit.setText(data[0])
        y.lineEdit_2.setText(data[1])
        y.lineEdit_3.setText(data[2])
        y.lineEdit_4.setText(data[3])
        y.pushButton_2.clicked.connect(y.closeMG)
        
        y.pushButton.clicked.connect(y.saveMG)
        y.pushButton.clicked.connect(self.setsender)
        w.exec()
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        self.SendEmailBox.setDisabled(True)
        self.emailTextBox.clear()
                    
        
    def browseFile(self):
        
        self.excelfilpath, _ = QFileDialog.getOpenFileName(None, "Open Excel File", "", "Excel Files (*.xls *.xlsx);;All Files (*)")
        
        if self.excelfilpath:
            try:
                self.readbrowsedFile(self.excelfilpath)
                self.IndexNumber.setText('1')
                self.automModeCheck()
            except IndexError:
                pass

            
    def readbrowsedFile(self,path):
        self.recipiientsFileText.setText(path)
        self.readrecipientsfromexcel(path)
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        self.SendEmailBox.setDisabled(True)
        self.emailTextBox.clear()
        self.activeModeLabel.setText('Automatic Mode')
        
        with open('.\\Resources\\lastNumbersFile.txt','w') as w:
            w.write('')
            w.write(path)
        w.close()
        
        with open('.\\Resources\\lastNumbersFile.txt','r') as n:
            p = n.read()
        n.close()
        
        try:
            numbersExcel = openpyxl.load_workbook(p.replace('"',''))
            nubmersSheet = numbersExcel.worksheets[0]
        
            self.numbers = []
            row = 0
            while True:
                row+=1
                cell = 'B'+ str(row)
                if type(nubmersSheet[cell].value)==str:
                    self.numbers.append(nubmersSheet[cell].value)
                    continue
                else:
                    break
            
            self.numbers = list(set(self.numbers))
            with open('.\\Resources\\currentNubmers.txt','w') as g:
                g.write('')
                for i in self.numbers:
                    g.writelines(i+'\n')
            g.close()
            self.currentNumberBox.setText(self.numbers[0])
            self.currentCellLabel.setText('B1')
            numbersExcel.close()
            self.row = 0
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.emailTextBox.clear()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
        except UnboundLocalError:
            self.wrongsheet()
        except FileNotFoundError:
            self.wrongFile()
        self.readNumbers()
            


    def openNubers(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('.\\Resources\\currentNubmers.txt'))
        
    def readNumbers(self):
        
            with open('.\\Resources\\currentRecipients.txt','r') as g:
                n = g.readlines()
                self.currentNumbers =[]
                for i in n:
                    b = i.replace('\n','')
                    self.currentNumbers.append(b)
            g.close()
            try:
                self.currentNumberBox.setText(self.currentNumbers[0])
            except IndexError:
                pass
            self.currentCellLabel.setText('B1')
            self.row = 0
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.emailTextBox.clear()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
    
            
    def wrongsheet(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('icon.png'))  # You can use other icons like Information, Critical, etc.
        msg.setWindowTitle('Error In Excel File')       # Title of the MessageBox
        msg.setText('The sheet that contains numbers in the excel file \nDoes Not Exist')        # Main message text
        msg.setStandardButtons(QtWidgets.QMessageBox().Ok)
        msg.exec_()
        
    def wrongFile(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('icon.png'))  # You can use other icons like Information, Critical, etc.
        msg.setWindowTitle('Error In Excel File')       # Title of the MessageBox
        msg.setText('The Excel file that contains numbers\nMust have name of "numbers" and with .xslx extention\nand be present in app folder')        # Main message text
        msg.setStandardButtons(QtWidgets.QMessageBox().Ok)
        msg.exec_()
        
    def setsender(self): 
        # Read Sender
        with open('.\\Resources\\mailGun.txt','r') as b:
            n = b.readlines()
            data=[]
            for i in n:
                f = i.replace('\n','')   
                data.append(f)
        b.close()
        
        sender = data[2] + ' <' + data[3] + '>' 
        self.emailToBox.setText(sender)
            
            
    def readRecipients(self):
        with open('.\\Resources\\currentRecipients.txt','r') as h:
            emailss = h.readlines()
            emails = []
            for i in emailss:
                n=i.replace('\n','')
                emails.append(n)
        
        h.close()
        self.recipient1box.setText(emails[0])
        self.recipient2box.setText(emails[0])
        self.recipient3box.setText(emails[0])
     
    def witerecipients(self):
        
        rec1 = self.recipient1box.text() 
        rec2 = self.recipient2box.text() 
        rec3 = self.recipient3box.text() 

        
        with open('.\\Resources\\currentRecipients.txt','w') as n:
            n.write('')
            n.writelines(rec1+'\n')
            n.writelines(rec2+'\n')
            n.writelines(rec3+'\n')

        n.close()

    
    def readTails(self):
        with open('.\\Resources\\tails.txt','r') as h:
            tails = h.readlines()
            self.tailss=[]
            for tail in tails:
                n= tail.replace('\n','')
                self.tailss.append(n)
            
            tailsboxes = [self.rece1tail,self.rece2tail,self.rece3tail]
            n=0
            for i in self.tailss:
                tailsboxes[n].setText(i)
                n=n+1
            
        h.close()
        
    def writeTails(self):
        
        self.tail1 = self.rece1tail.text()
        self.tail2 = self.rece2tail.text()
        self.tail3 = self.rece3tail.text()
        self.tails = [self.tail1,self.tail2,self.tail3]
        with open('.\\Resources\\tails.txt','w') as w:
            w.write('')
            for tail in self.tails:
                w.writelines(tail+'\n')
        w.close()
            
    def readrecipientsfromexcel(self,path):
        try:
            recipientsExcel = openpyxl.load_workbook(path)
        except:
            self.wrongFile
        recipientsSheet = recipientsExcel.worksheets[0]
        self.recipients = []
        row = 0
        
        try:
            while True:
                row+=1
                cell = 'B'+ str(row)
                if type(recipientsSheet[cell].value)==str:
                    self.recipients.append(recipientsSheet[cell].value.replace('-',''))
                    continue
                else:
                    break
        except TypeError:
            pass
        
        
        self.recipients = list(set(self.recipients))
        
        with open('.\\Resources\\currentRecipients.txt','w') as g:
            g.write('')
            for i in self.recipients:
                g.writelines(i.replace('-','')+'\n')
        g.close()
        
        recipientsExcel.close()
        
        self.readRecipients()
        
        self.emailrow = 0
        
        self.nextEmaills.show()
        self.PrevEmails.show()
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        self.SendEmailBox.setDisabled(True)
        self.emailTextBox.clear()
        
        
    def prepareEmail(self):
        
        self.emailTextBox.clear()
        
        with open('.\\Resources\\email.txt','r') as e:
            email = e.read()
        e.close()
        
        number = self.currentNumberBox.text()
        emailFrom = self.emailToBox.text()
        self.receivers = []
        
        if (len(self.recipient1box.text())!=0 and len(self.rece1tail.text())!=0):
            self.receivers.append(self.recipient1box.text()+'@'+self.rece1tail.text())
        if (len(self.recipient2box.text())!=0 and len(self.rece2tail.text())!=0):
            self.receivers.append(self.recipient2box.text()+'@'+self.rece2tail.text())
        if (len(self.recipient3box.text())!=0 and len(self.rece3tail.text())!=0):
            self.receivers.append(self.recipient3box.text()+'@'+self.rece3tail.text())
        self.subject = email.split(':')[1].split('\n')[0]
        self.body=email.split(':')[-1]
        # body = b.replace('\n','<br>')+'<br><br>&nbsp&nbsp'+number
        receiversstr =''
        for i in self.receivers:
            receiversstr = receiversstr+'\t'+i+'\n'
        emaillines = ['From: '+emailFrom,"To: "+receiversstr,"Subject: "+self.subject,'Body: '+self.body]
        
        for line in emaillines:
            self.emailTextBox.append(line+'\n')
            
        self.emailPreparedText.show()
        self.emailSentText.hide()
        self.SendEmailBox.setEnabled(True)
        self.writeTails()
        
        
    def sendEmail(self):
        
        number = self.currentNumberBox.text()
        sender = self.emailToBox.text()
        receips = self.receivers
        subject = self.subject
        body = self.body
        
        EmailSender(sender,receips,subject,body,number)
        self.SendEmailBox.setDisabled(True)
        self.emailSentText.show()
        with open('.\\Resources\\lastIndex.txt','w') as l:
            l.write(self.IndexNumber.text())
        l.close()
        
    def nextnumber(self):
        self.nextrow = self.row +1
        if self.nextrow <= len(self.currentNumbers)-1:
            self.currentNumberBox.setText(self.currentNumbers[self.nextrow])
            self.currentCellLabel.setText('B'+str(self.nextrow+1))
            self.row+=1
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
        
    def previousnumber(self):
        self.prevrow = self.row -1
        
        if self.prevrow >=0:
            self.currentNumberBox.setText(self.currentNumbers[self.prevrow])
            self.currentCellLabel.setText('B'+str(self.prevrow+1))
            self.row-=1
            self.emailPreparedText.hide()
            self.emailSentText.hide()
            self.SendEmailBox.setDisabled(True)
            self.emailTextBox.clear()
        
    def updatenumbers(self):
        self.readNumbers()
        self.emailPreparedText.hide()
        self.emailSentText.hide()
        self.SendEmailBox.setDisabled(True)
        self.emailTextBox.clear()
        
    def automMode(self):
                
        class nativeAuto(Ui_Dialog):
            def __init__(self) -> None:
                super().__init__()
                
            def saved(self):
                self.label.show()
                varynumb = x.varyNumber.isChecked()
                varyrece = x.varyRecip.isChecked()
                with open('.\\Resources\\autoMode.txt','w') as a:
                    a.writelines(str(varynumb)+'\n')
                    a.writelines(str(varyrece))
                a.close()
                
            def change(self):
                self.label.hide()
            
        
        x = nativeAuto()
        w = QtWidgets.QDialog()
        w.setWindowIcon(QtGui.QIcon('icon.png'))
        x.setupUi(w)
        x.label.hide()
        
        with open('.\\Resources\\autoMode.txt','r') as a:
            au = a.readlines()
        a.close()
        
        if 'True' in au[0]:
            x.varyNumber.setChecked(True)
        if 'True' in au[1]:
            x.varyRecip.setChecked(True)
            
        x.pushButton_2.clicked.connect(w.close)
        x.pushButton.clicked.connect(x.saved)
        x.pushButton.clicked.connect(self.automModeCheck)
        x.varyNumber.clicked.connect(x.change)
        x.varyRecip.clicked.connect(x.change)
        w.exec()
        
    def automModeCheck(self):
        self.activeModeLabel.setText('Automatic Mode')
        
        self.varyRecp=0
        self.varyNum=0
        with open('.\\Resources\\autoMode.txt','r') as a:
            au = a.readlines()
        a.close()

        if 'True' in au[0]:
            self.varyNum = 1
            self.StopAutomaticButton.setText('Start')
            self.StopAutomaticButton.show()
            self.activeModeLabel.show()
            self.mode = 0
            
        if 'True' in au[1]:
            self.varyRecp = 1
            self.StopAutomaticButton.setText('Start')
            self.StopAutomaticButton.show()
            self.activeModeLabel.show()
            self.mode = 0
            
        if ('False' in au[0] and 'False' in au[1]):
            self.StopAutomaticButton.hide()
            self.activeModeLabel.hide()
        
    def stopAutoMode(self):
        
        # Start
        if self.mode==0:
            with open('.\\Resources\\runAuto.txt','w') as a:
                a.write('')
            a.close()
            
            self.mode=1
            self.StopAutomaticButton.setText('Stop')
            self.activeModeLabel.setText('Running...')

            if (self.varyNum==1 and self.varyRecp==1 and self.nextEmaills.isVisible()):
                self.press_order = [self.NextnumberButton,self.nextEmaills, self.prepareEmailButton,self.SendEmailBox]
                self.prepareEmail()
                self.sendEmail()
                self.timer.start(1000)

            elif (self.varyNum==1 and self.varyRecp==0):
                self.press_order = [self.NextnumberButton,self.prepareEmailButton,self.SendEmailBox]
                self.prepareEmail()
                self.sendEmail()
                self.timer.start(1000)
            elif (self.varyRecp==1 and self.varyNum==0):
                if self.nextEmaills.isVisible():
                    self.press_order = [self.nextEmaills,self.prepareEmailButton,self.SendEmailBox]
                    self.prepareEmail()
                    self.sendEmail()
                    self.timer.start(1000)
                else:
                    self.recipiientsFileText.setText('No File for Recipients to Vary')
                    self.activeModeLabel.setText('Upload Recipients')
                    self.stopAutoMode()
            elif (self.varyRecp==1 and self.varyNum==1 and not((self.nextEmaills.isVisible()))):
                  self.recipiientsFileText.setText('No File for Recipients to Vary')
                  self.activeModeLabel.setText('Upload Recipients')
                  self.stopAutoMode()
            else:
                self.activeModeLabel.setText('Wrong Settings')
                self.stopAutoMode()

                
            # QTimer to simulate automatic pressing
            self.current_index = 0
            
        # Stop 
        elif self.mode==1:
            with open('.\\Resources\\runAuto.txt','w') as a:
                a.write('stop')
            a.close()
            self.mode=0
            self.StopAutomaticButton.setText('Start')
            
    def auto_press(self):
        
        with open('.\\Resources\\runAuto.txt','r') as a:
                s = a.read()
        a.close()
     
        if 'stop' in s:
            self.timer.stop()
            return
       
        elif self.emailrow+1==len(self.recipients):
            self.prepareEmail()
            self.sendEmail()
            self.timer.stop()
            self.StopAutomaticButton.click()
            self.activeModeLabel.setText('Finished')
            self.StopAutomaticButton.hide()
            self.emailSentText.show()
            self.SendEmailBox.setDisabled(True)

        # Emit click signal to simulate press
        self.press_order[self.current_index % len(self.press_order)].click()

        self.current_index += 1
        
    def openemail(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('.\\Resources\\email.txt'))
        
    def  opennumbersSheet(self):
        try:
            QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(self.recipiientsFileText.text()))
        except AttributeError:
            pass
    
    def openrecipientsFile(self):
        try:
            QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(self.recipiientsFileText.text()))
        except AttributeError:
            pass
    def openLogFile(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('Log.txt'))
    
    def resetinterface(self):
        
        self.emailTextBox.clear()
        
    def closeprogram(self):
        
        self.witerecipients()
        with open('.\\Resources\\currentNubmers.txt','w') as g:
                g.write('')
        g.close()
        
        mainuiwindow.close()
       
        

if __name__=='__main__':
    app= QtWidgets.QApplication([])
    mainuiwindow = QtWidgets.QMainWindow()
    mainuiwindow.setWindowIcon(QtGui.QIcon('icon.png'))
    x = MainWindow()
    x.mainView(mainuiwindow)
    mainuiwindow.show()
    app.exec_()
    
    
# This is a program to send emails automatically with user interface 
# Author: Developer and Enfineer Gad Badr @ https://devgadbadr.github.io/personal-website/