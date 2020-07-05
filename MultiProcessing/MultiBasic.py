import multiprocessing
import logging
import time

#logging.basicConfig(level=logging.DEBUG, format="(%(processName)-10s) %(message)s")


print(__name__)

print("i am being called")
print(__name__)
def process_handeler():
    logging.debug("module name is %s", __name__)
    logging.debug("started")


if __name__ == "__main__":
    p = multiprocessing.Process(name="anil", target=process_handeler)
    p.start()
    

