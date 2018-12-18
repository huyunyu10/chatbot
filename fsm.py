from transitions.extensions import GraphMachine

from utils import send_text_message

import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False
    
    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '咖啡'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '酒'
        return False
    
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '單品'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '義式'
        return False     
    
    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '調酒'
        return False
    
    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '純飲'
        return False
    
    def is_going_to_return_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'r'
        return False    
    
    def is_going_to_return_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'r'
        return False
    
    def is_going_to_return_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'r'
        return False
   
    def is_going_to_return_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'r'
        return False 

    def on_enter_user(self, event):
        print("輸入help以獲得功能介紹")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "輸入help以獲得功能介紹\n"
									+"或是開始挑選您的飲料")
    
    def on_enter_help(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "此為大人的飲料選擇器\n"
                                     +"輸入 咖啡 可以幫您隨機推薦一款咖啡\n"
                                     +"輸入 酒 可以幫您隨機推薦一款酒品\n")
        send_text_message(sender_id, "請輸入 quit 以回到最初選項")
             
    def on_enter_state1(self, event):
        print("此為咖啡的選項\n"
                                     +"輸入 單品 可以幫您隨機推薦一款單品咖啡\n"
                                     +"輸入 義式 可以幫您隨機推薦一款義式調飲\n"
                                     +"輸入 quit 可以回最初選項\n")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "此為大人的飲料選擇器\n"
                                     +"輸入 單品 可以幫您隨機推薦一款咖啡\n"
                                     +"輸入 義式 可以幫您隨機推薦一款酒品\n"
                                     +"輸入 quit 可以回最初選項\n")
         
    def on_enter_state2(self, event):
        print("此為酒的選項\n"
                                     +"輸入 調酒 可以幫您隨機推薦一款調酒\n"
                                     +"輸入 純飲 可以幫您隨機推薦一款純飲\n"
                                     +"輸入 quit 可以回最初選項\n")
        sender_id = event['sender']['id']
        send_text_message(sender_id, "此為酒的選項\n"
                                     +"輸入 調酒 可以幫您隨機推薦一款調酒\n"
                                     +"輸入 純飲 可以幫您隨機推薦一款純飲\n"
                                     +"輸入 quit 可以回最初選項\n")

    
    def on_enter_state3(self, event):
        f1 = open('coffee/scaa.txt','r')
        rnd = random.randint(1,len(f1.readlines()))
        f1.close()
        f1 = open('coffee/scaa.txt','r')
        line = f1.readlines()[rnd-1]
        sender_id = event['sender']['id']
        send_text_message(sender_id, line)
        send_text_message(sender_id, "輸入 r 會幫您重新推薦一次")
        send_text_message(sender_id, "輸入 quit 可以回最初選項")
    
    def on_enter_state4(self, event):
        f1 = open('coffee/espresso.txt','r')
        rnd = random.randint(1,len(f1.readlines()))
        f1.close()
        f1 = open('coffee/espresso.txt','r')
        line = f1.readlines()[rnd-1]
        sender_id = event['sender']['id']
        send_text_message(sender_id, line)
        send_text_message(sender_id, "輸入 r 會幫您重新推薦一次")
        send_text_message(sender_id, "輸入 quit 可以回最初選項")
    
    def on_enter_state5(self, event):
        f1 = open('liquor/cocktail.txt','r')
        rnd = random.randint(1,len(f1.readlines()))
        f1.close()
        f1 = open('liquor/cocktail.txt','r')
        line = f1.readlines()[rnd-1]
        sender_id = event['sender']['id']
        send_text_message(sender_id, line)
        send_text_message(sender_id, "輸入 r 會幫您重新推薦一次")
        send_text_message(sender_id, "輸入 quit 可以回最初選項")    
    
    def on_enter_state6(self, event):
        f1 = open('liquor/straight.txt','r')
        rnd = random.randint(1,len(f1.readlines()))
        f1.close()
        f1 = open('liquor/straight.txt','r')
        line = f1.readlines()[rnd-1]
        sender_id = event['sender']['id']
        send_text_message(sender_id, line)
        send_text_message(sender_id, "輸入 r 會幫您重新推薦一次")
        send_text_message(sender_id, "輸入 quit 可以回最初選項")    
   
    def back_to_init(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'quit'
