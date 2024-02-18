"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
import multiprocessing
# import random
from concurrent.futures import ProcessPoolExecutor
from time import sleep

from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn

from pkscreener.classes.PKTask import PKTask

# def long_running_fn(progress, task_id):
#     len_of_task = random.randint(3, 20)  # take some random length of time
#     for n in range(0, len_of_task):
#         # sleep(1)  # sleep for a bit to simulate work
#         progress[task_id] = {"progress": n + 1, "total": len_of_task}


def scheduleTasks(tasksList=[], showProgressBars=False):
    n_workers = multiprocessing.cpu_count() - 1  # set this to the number of cores you have on your machine

    with Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        TimeElapsedColumn(),
        refresh_per_second=1,  # bit slower updates
    ) as progress:
        if len(tasksList) == 0:
            raise ValueError("No tasks in the tasksList!")
        for task in tasksList:
            if not isinstance(task, PKTask):
                raise ValueError("Each task in the tasksList must be of type PKTask!")

        futures = []  # keep track of the jobs
        with multiprocessing.Manager() as manager:
            # this is the key - we share some state between our 
            # main process and our worker functions
            _progress = manager.dict()
            overall_progress_task = progress.add_task("[green]Pending jobs progress:")

            with ProcessPoolExecutor(max_workers=n_workers) as executor:
                for task in tasksList:  # iterate over the jobs we need to run
                    # set visible false so we don't have a lot of bars all at once:
                    task_id = progress.add_task(f"Task :{task.taskName}", visible=False)
                    futures.append(executor.submit(task.long_running_fn, _progress, task_id))

                # monitor the progress:
                while (n_finished := sum([future.done() for future in futures])) < len(
                    futures
                ):
                    progress.update(
                        overall_progress_task, completed=n_finished, total=len(futures)
                    )
                    for task_id, update_data in _progress.items():
                        latest = update_data["progress"]
                        total = update_data["total"]
                        # update the progress bar for this task:
                        progress.update(
                            task_id,
                            completed=latest,
                            total=total,
                            visible=latest < total,
                        )

                # raise any errors:
                for future in futures:
                    future.result()
