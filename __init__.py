# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from mycroft.skills import MycroftSkill, intent_handler
from mycroft.util import play_mp3
from os.path import join, dirname


class MonkeyPatchTester(MycroftSkill):
    def initialize(self):
        if not self.settings.get("first_patch"):
            self.check_monkey_patches()

    def check_monkey_patches(self):
        monkey = False
        try:
            monkey = self.monkey_patched
        except:
            pass
        if monkey:
            self.log.info("Mycroft is monkey patched! WARRANTY VOID")
            sound = join(dirname(__file__), "res", "monkey.mp3")
            play_mp3(sound).wait()
            self.settings["first_patch"] = True
        else:
            self.log.info("Mycroft is NOT monkey patched!")
        return monkey

    @intent_handler("monkey_test.intent")
    def handle_monkey_test_intent(self, message):
        if self.check_monkey_patches():
            self.speak_dialog("yes")
        else:
            self.speak_dialog("no")


def create_skill():
    return MonkeyPatchTester()
