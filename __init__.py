from mycroft import MycroftSkill, intent_file_handler


class EventTracking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tracking.event.intent')
    def handle_tracking_event(self, message):
        self.speak_dialog('tracking.event')


def create_skill():
    return EventTracking()

