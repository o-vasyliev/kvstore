import kv_helpers
import threading
import time

kv = kv_helpers.KVstore()


def test_vals():
    i = 0

    while i < 10000:
        kv.put("lol", "kek")
        # print(kv.get("lol"))
        i += 1


if __name__ == "__main__":
    start_time = time.time()
    for i in range(2):
        t = threading.Thread(target=test_vals)
        t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    print("--- %s seconds ---" % (time.time() - start_time))
