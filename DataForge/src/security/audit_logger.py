# src/security/audit_logger.py
import logging

class AuditLogger:
    def __init__(self, log_file='audit.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger()

    def log(self, message):
        self.logger.info(message)
