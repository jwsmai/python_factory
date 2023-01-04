from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


"""
concurrent 包中提供了 ThreadPoolExecutor 和 ProcessPoolExecutor 类，分别对应多线程和多进程模型。
关于两种模型的使用及推荐并发数，我们有一个经验：

CPU 密集型任务，推荐使用多进程模型，以利用 CPU 的多个核心，max_workers 应设置为 CPU 核数；
IO 密集型任务，多核 CPU 不会提高性能，所以推荐使用多线程模型，可以省下多进程带来的资源开销，max_workers 可以尽可能设置多一些。
"""


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for cc in sorted(cc_list):
            # executor.submit方法排定可调用对象的执行时间，然后返回一个future，表示这个待执行的操作。
            future = executor.submit(download_one, cc)
            # 存储各个future，后面传给as_completed函数。
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        # as_completed函数在future运行结束后产出future。
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)
