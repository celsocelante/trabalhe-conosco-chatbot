# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class OrderForm(Action):
    """Example of a custom form action"""

    def name(self):
        """Unique identifier of the form"""
        return "form_order"

    def required_slots(self, tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return {"coffe_size"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return ["coffe_size": self.from_entity(intent='choose', entity='coffe_size')]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled."""
        try:
            coffe_size = tracker.get_slot('coffe_size')
            r = requests.post ('/basket/coffe/add', data=coffe_size)
            if r.status_code == requests.codes.ok:
                dispatcher.utter_message(template="utter_ticket")
            else:
                dispatcher.utter_message(template="utter_ticket_error")
        except:
            dispatcher.utter_message(template="utter_ticket_error")
        return []


class UserForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        """Unique identifier of the form"""
        return "user_form"

    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ["name", "email", "cpf"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A list of required slots that the form has to fill"""
        
        return {
            "name": self.from_text(intent='inform_name'),
            "email": [
                self.from_entity(intent='inform_name', entity="email"),
                self.front_intent(intent='inform_email', entity="email"),
                self.fron_text(intent='inform_email', not_intent="email")
                ],
            "cpf": self.from_entity(entity="cpf")
        }
    
    def validate_cpf(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
                    ) -> Dict[Text, Any]:
        """Validate cpf value."""
        regex = r'\d{3}.\d{3}.\d{3}-\d{2}'
        if (re.findall(regex,value)):
            return {"cpf": value}
        else:
            dispatcher.utter_message(template="utter_wrong_cpf")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cpf": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled."""
        return []

