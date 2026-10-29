"""In-memory refresh-token rotation example."""


class RefreshTokens:
    def __init__(self):
        self.active = {"session-1": {"refresh-a"}}

    def rotate(self, session_id: str, presented: str):
        active_for_session = self.active.get(session_id, set())
        if presented not in active_for_session:
            return None
        replacement = presented + "-next"
        # Bug: the old token remains active and can be replayed.
        active_for_session.add(replacement)
        return replacement
