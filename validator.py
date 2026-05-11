# ==========================================
# VALIDATION LAYER
# ==========================================

def validate_input(confidence, correctness):

    # Missing confidence
    if confidence is None:

        confidence = 0.5

    # Clamp values
    confidence = max(0.0, min(1.0, confidence))

    correctness = max(0, min(10, correctness))

    return confidence, correctness