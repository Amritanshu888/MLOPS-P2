## Whenever we face any exception we should be able to create our own custom exception to handle it
import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):  ## We are making a class
    def __init__(self,error_message,error_details:sys):  ## init method here we are taking two values : error_message and error_details which is coming from system , that is the reason we have imported sys over here.
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info() ## Here we are taking 3 informations , first two are not required , exc_tb (third info is required). exc_tb ---> execution_tb gives our entire execution details , error_details is coming as a sys parameter , it is a parameter from system.

        self.lineno=exc_tb.tb_lineno   ## Line number will be available inside this variable
        self.file_name=exc_tb.tb_frame.f_code.co_filename  ## Even ur filename will be available inside this variable

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name, self.lineno, str(self.error_message))

if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)         