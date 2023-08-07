class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = dict()
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        # create a max heap of the frequency
        # of the task occuring using the map
        hq = list()
        for task, count in counter.items():
            heappush(hq, (-count, task)) # trick: use min heap as max heap
        
        time = 0
        while hq:
            tmp = []
            for _ in range(n + 1): # units are inclusive hence n+1
                # add all tasks to the temp list
                # if there are tasks to be processed
                # in the queue, note that for this n
                # cycles, we're not pushing processed
                # items back in the queue but rather in the
                # tmp list so that they don't appear before n
                # cycles have been passed.
                if hq:
                    tmp.append((heappop(hq)))
                
            # but once we've done n cycles from the
            # queue, we can safely add the processed
            # tasks back to the queue to be processed
            # again if they have repititions left (count)
            for count, task in tmp:
                if count+1 < 0:
                    heappush(hq, (count+1, task))
            
            # for every cycle, we will add n+1 cycles to the total
            # time because that's the max number of cycles you can
            # perform at a time without repeating characters
            # BUT for the last few tasks, there can be <n tasks
            # in the queue and we would've put them inside tmp
            # so only in that case, we'll check if queue is empty
            # and if so, we'll add len(tmp) to the overall time
            time += len(tmp) if not hq else n + 1
                
        return time
