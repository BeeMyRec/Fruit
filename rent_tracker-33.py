# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: RentTracker
import bisect, datetime, time


def undo_last_action(history):
    """Откат последнего действия (если это была запись)."""
    if not history:
        return False
    last = history[-1]
    if last["kind"] != "rental":
        return False
    idx = bisect.bisect_left(history, {"id": last["id"], "kind": "rental"}) - 1
    if idx < 0:
        return False
    undo = history[idx]["undo"]
    if not undo:
        return False
    entry = list(undo)
    entry[3] += time.time()
    bisect.insort(history, entry)
    return True
