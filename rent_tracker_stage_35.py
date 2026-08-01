# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RentTracker
def get_next_action(state):
    """Returns a suggestion for the next step based on the current state."""
    if not state.get('items'):
        return "Add your first item to start tracking."
    
    active = [i for i in state['items'] if i['returned'] is False]
    completed = [i for i in state['items'] if i['returned'] is True]
    
    if not active:
        return f"All {len(completed)} items returned. Start a new item."
    
    overdue = [i for i in active if (state.get('today') or '2025-12-28').date() > datetime.fromisoformat(i['due_date']).date()]
    
    if overdue:
        names = ', '.join(f"{i['name']} ({i['client']})" for i in overdue[:3])
        return f"⚠️ {len(overdue)} overdue item(s): {names}"
    
    if active and len(active) >= 5:
        return "You have many items out. Consider organizing or archiving old ones."
    
    if state.get('clients') < 2:
        return "Add another client to expand your rental network."
    
    if not state.get('history'):
        return "Log an event (rent, return, note) to build history."
    
    return "Everything looks good. Continue adding items or clients!"
