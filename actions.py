# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
# import covid_details as cd


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return [AllSlotsReset()]

class ActionCovidMailForm(FormAction):

    def name(self) -> Text:
        return "covid_mail_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["NAME", "CITY", "MAIL"]

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker, domain: Dict[Text, any])->List[Dict]:
        print("submit invoked")
        name = tracker.get_slot('NAME')
        city = tracker.get_slot('CITY')
        mail = tracker.get_slot('MAIL')
        dispatcher.utter_message(templates="utter_mail_send",
                                 name = name,
                                 city = city,
                                 mail = mail)
        print(name, city, mail)
        # cd.mail_send(name,mail,city)
        return [SlotSet("NAME", None), SlotSet("MAIL", None), SlotSet("CITY", None)]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        print("slot_mapping invoked")
        return {"name": [self.from_entity(entity="NAME", intent="my_name"),
                         self.from_text()],
                "city": [self.from_entity(entity="CITY", intent="city"),
                         self.from_text()],
                "mail": [self.from_entity(entity="MAIL", intent="mail"),
                         self.from_text()]}

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, any]) -> List[Dict[Text, any]]:
    #     print("run method covid")
    #     return []
