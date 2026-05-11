# ==========================================
# ADAPTIVE DECISION ENGINE
# ==========================================

import statistics

from database import (
    initialize_user,
    get_user,
    update_user
)

class AdaptiveEngine:

    def __init__(self):

        self.levels = ["easy", "medium", "hard"]

    # --------------------------------------
    # Adaptation Score
    # --------------------------------------

    def calculate_score(self, confidence, correctness):

        normalized = correctness / 10

        score = (
            (0.6 * normalized)
            +
            (0.4 * confidence)
        )

        return round(score, 2)

    # --------------------------------------
    # Decision Rules
    # --------------------------------------

    def decision_engine(self, confidence, correctness):

        # High confidence + high correctness
        if confidence > 0.75 and correctness >= 8:

            return (
                "increase",
                "Excellent performance"
            )

        # Low confidence + low correctness
        if confidence < 0.4 and correctness < 5:

            return (
                "decrease",
                "Weak performance"
            )

        # Contradictory signals
        if confidence > 0.8 and correctness < 4:

            return (
                "maintain",
                "Possible overconfidence"
            )

        # Default
        return (
            "maintain",
            "Balanced performance"
        )

    # --------------------------------------
    # Stability Layer
    # --------------------------------------

    def apply_stability(self, user, action):

        if action == "increase":

            user["increase_streak"] += 1
            user["decrease_streak"] = 0

            if user["increase_streak"] >= 2:

                user["increase_streak"] = 0

                return "increase"

            return "maintain"

        elif action == "decrease":

            user["decrease_streak"] += 1
            user["increase_streak"] = 0

            if user["decrease_streak"] >= 2:

                user["decrease_streak"] = 0

                return "decrease"

            return "maintain"

        return "maintain"

    # --------------------------------------
    # Difficulty Transition
    # --------------------------------------

    def update_difficulty(self, user, action):

        index = self.levels.index(
            user["difficulty"]
        )

        if action == "increase":

            index = min(index + 1, 2)

        elif action == "decrease":

            index = max(index - 1, 0)

        user["difficulty"] = self.levels[index]

    # --------------------------------------
    # Main Adaptation Logic
    # --------------------------------------

    def adapt(
        self,
        user_id,
        confidence,
        correctness
    ):

        initialize_user(user_id)

        user = get_user(user_id)

        # Score
        score = self.calculate_score(
            confidence,
            correctness
        )

        # Store history
        user["history"].append(score)

        # Rolling average
        avg_score = round(
            statistics.mean(user["history"]),
            2
        )

        # Decision
        action, reason = self.decision_engine(
            confidence,
            correctness
        )

        # Stability
        stable_action = self.apply_stability(
            user,
            action
        )

        # Update difficulty
        self.update_difficulty(
            user,
            stable_action
        )

        # Save user
        update_user(user_id, user)

        return {

            "user_id": user_id,

            "confidence": confidence,

            "correctness": correctness,

            "score": score,

            "average_score": avg_score,

            "decision": stable_action,

            "difficulty": user["difficulty"],

            "reason": reason
        }