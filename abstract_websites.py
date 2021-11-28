from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent


class AbstractWebsites:

    def is_pwned(self, email):
        pass

    @staticmethod
    def generate_user_agent():
        software_names = [SoftwareName.FIREFOX.value]
        os = [OperatingSystem.LINUX.value, OperatingSystem.WINDOWS.value, OperatingSystem.ANDROID.value]
        user_agent_rotator = UserAgent(software_names=software_names,
                                       operating_systems=os,
                                       limit=100)
        return user_agent_rotator.get_random_user_agent()
