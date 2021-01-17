from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        self.mensagem = 'Bom dia forneças os dados pedidos'
        self.grupos = ['TESTE']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensaguens(self):
        # title="TESTE"
        # <div tabindex="-1" class="DuUXI">
        # <span data-testid="send" data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo.click()
            time.sleep(3)

            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(3)

            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)

            botao_enviar.click()
            time.sleep(5)

bot = whatsappBot()
bot.EnviarMensaguens()