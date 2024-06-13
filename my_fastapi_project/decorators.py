import time
import logging
import json

logging.basicConfig(level=logging.INFO)

def send_to_apm(trace_data):
    logging.info(f"Sending trace data to APM: {trace_data}")

def trace(func):
    def wrapper(*args, **kwargs):
        trace_data = {
            'function': func.__name__,
            'args': args,
            'kwargs': kwargs,
            'start_time': time.time(),
            'ip_address': '127.0.0.1'
        }
        
        try:
            result = func(*args, **kwargs)
            trace_data['result'] = result
        except Exception as e:
            trace_data['exception'] = str(e)
            raise
        finally:
            trace_data['end_time'] = time.time()
            trace_data['duration'] = trace_data['end_time'] - trace_data['start_time']
            send_to_apm(json.dumps(trace_data, indent=4))
        
        return result
    return wrapper
