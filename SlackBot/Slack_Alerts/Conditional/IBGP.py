import logging
import math
from datetime import datetime
from SlackBot.External import External_Config
from SlackBot.Slack_Alerts.Conditional.Base import Base_Conditional

logger = logging.getLogger(__name__)

class IBGP(Base_Conditional):
    def __init__(self, product_name, variables):    
        super().__init__(product_name, variables)
        
    def ibgp_input(self):
        print("driving input for hvnr return score and realted calculations return long/short")
