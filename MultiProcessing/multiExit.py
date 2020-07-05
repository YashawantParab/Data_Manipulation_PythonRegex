import multiprocessing
import sys
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="(%(processName)-10s) %(message)s")


def exit_error():
    exit(2)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError("I want to create an error!")


def terminated():
    time.sleep(2)


if __name__ == "__main__":
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        logging.debug("starting process %s", f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        logging.debug("%s exitcode = %s", j.name, j.exitcode)

