from Ferramentas_Producao.modules.utils.factories.utilsFactory import UtilsFactory

class ProdToolsCtrl:

    def __init__(
            self,
            messageFactory=UtilsFactory().createMessageFactory()
        ):
        super(ProdToolsCtrl, self).__init__()
        self.messageFactory = messageFactory

    def showHtmlMessageDialog(self, parent, title, message):
        htmlMessageDlg = self.messageFactory.createMessage('HtmlMessageDialog')
        htmlMessageDlg.show(parent, title, message)

    def showInfoMessageBox(self, parent, title, message):
        messageDlg = self.messageFactory.createMessage('InfoMessageBox')
        messageDlg.show(parent, title, message)
    
    def showErrorMessageBox(self, parent, title, message):
        messageDlg = self.messageFactory.createMessage('ErrorMessageBox')
        messageDlg.show(parent, title, message)