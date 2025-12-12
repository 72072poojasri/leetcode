class Solution:
    def countMentions(self, numberOfUsers, events):
        from collections import defaultdict

        # Bucket events by timestamp (chronological processing).
        # For each timestamp t we keep two lists: offline events and message strings.
        buckets = defaultdict(lambda: {"offline": [], "message": []})
        timestamps = set()

        for typ, t_str, payload in events:
            t = int(t_str)
            timestamps.add(t)
            if typ == "OFFLINE":
                # payload is id as string
                uid = int(payload)
                buckets[t]["offline"].append(uid)
            else:
                buckets[t]["message"].append(payload)

        # We'll process timestamps in increasing numeric order
        times_sorted = sorted(timestamps)

        online = [True] * numberOfUsers
        nextOnlineTime = [0] * numberOfUsers  # if offline, time when they come back

        mentions = [0] * numberOfUsers

        for t in times_sorted:
            # 1) auto-recover users whose offline expired at or before t
            for u in range(numberOfUsers):
                if not online[u] and nextOnlineTime[u] <= t:
                    online[u] = True

            # 2) process all OFFLINE events at t (they become offline now and come back at t+60)
            for uid in buckets[t]["offline"]:
                # problem guarantees user is online at the time of their OFFLINE
                online[uid] = False
                nextOnlineTime[uid] = t + 60

            # 3) process all MESSAGE events at t (after offline changes)
            for msg in buckets[t]["message"]:
                if msg == "ALL":
                    # Mention all users (online or offline)
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif msg == "HERE":
                    # Mention only currently online users
                    for u in range(numberOfUsers):
                        if online[u]:
                            mentions[u] += 1
                else:
                    # explicit "id<number>" tokens separated by spaces (may repeat)
                    for token in msg.split():
                        if token.startswith("id"):
                            uid = int(token[2:])
                            mentions[uid] += 1

        return mentions