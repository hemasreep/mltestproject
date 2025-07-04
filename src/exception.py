import sys
from src.logger import logger



def error_message_detail(error,error_detail:sys):
     _, _, exc_tb = error_detail.exc_info()
     lineno = exc_tb.tb_lineno
     file_name = exc_tb.tb_frame.f_code.co_filename
     error_message="Error occurred in Python script: [{0}] at line [{1}] with message: [{2}]".format(file_name,lineno,str(error))
     logger.info(error_message)
     
     return error_message
     

    



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message =error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message 
   
   
   
if __name__=="__main__":
    try:
        
        a=1/0
        
    except Exception as e:
        logger.info("divide by xero")
        raise CustomException(e,sys)   
           