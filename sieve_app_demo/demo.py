from sieve_core import get_logger

def hello_demo():
    log = get_logger("demo")
    log.info("Hello from sieve-app-demo, using sieve-core logger!")
    return "hello from sieve-app-demo"

