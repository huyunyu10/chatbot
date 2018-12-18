from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'coffee'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'liquor'
        return False
    
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'scaa'
    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'espresso'
    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'cocktail'
    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'straight'

    def on_enter_state1(self, event):
        print("in state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "in state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")

    
    def on_enter_state3(self, event):
        print("in state3")

        sender_id = event['sender']['id']
        send_test_message(sender_id, "in state3")

    def on_enter_state4(self, event):
        print("in state4")

        sender_id = event['sender']['id']
        send_test_message(sender_id, "in state4")
    def on_enter_state5(self, event):
        print("in state5")

        sender_id = event['sender']['id']
        send_test_message(sender_id, "in state5")
    def on_enter_state6(self, event):
        print("in state6")

        sender_id = event['sender']['id']
        send_test_message(sender_id, "in state6")
    
    def back_to_init(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'quit'


