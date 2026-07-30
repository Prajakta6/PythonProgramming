import psutil
import logging

def DisplayProcessInformation():
    try:
        processes = psutil.process_iter(['pid', 'name', 'username'])
        logging.info("--------------------------------------------------")
        logging.info("Running Process Information")
        logging.info("--------------------------------------------------")

        for process in processes:
            try:
                info = process.info
                logging.info(
                    "PID : {} | Name : {} | User : {}".format(
                        info['pid'],
                        info['name'],
                        info['username']
                    ))
            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                logging.warning("Unable to access a process.")
    except Exception as e:
        logging.error(str(e))

def DisplayProcess(ProcessName):
    try:
        Flag = False
        logging.info("------------------------------------------")
        logging.info("Searching Process : {}".format(ProcessName))
        logging.info("------------------------------------------")

        for process in psutil.process_iter(['pid', 'name', 'username']):
            try:
                info = process.info
                if info['name'] is not None:
                    if info['name'].lower() == ProcessName.lower():
                        Flag = True
                        logging.info("Process Found")
                        logging.info("PID      : {}".format(info['pid']))
                        logging.info("Name     : {}".format(info['name']))
                        logging.info("Username : {}".format(info['username']))
                        logging.info("------------------------------------------")
            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass
        if Flag == False:
            logging.info("Process '{}' is not running.".format(ProcessName))

    except Exception as e:
        logging.error(str(e))