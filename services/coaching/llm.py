from services.config.workout_config import PROMPT


class LLMCoach:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.system_prompt = PROMPT

    def give_feedback(self, event, issue):
        prompt = f"Event: {event}"

        if issue:
            prompt += f" Form Issue: {issue}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history[-10:],
            {"role": "user", "content": prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.4,
            )
            text = response.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": text})
            return text
        except Exception as e:
            print("COACH LLM CONNECTION/API ERROR:", e)
            
            # Professional, context-aware fallback cues if Groq API is offline/unreachable
            fallback_responses = {
                "workout_started": "Welcome to your training session! Let's begin. Focus on your posture and pace.",
                "workout_completed": "Fantastic job completing your workout! Outstanding effort today.",
                "set_completed": "Excellent work completing that set! Take a brief rest before the next one.",
                "no_pose_detected": "Please step back into the camera frame so I can track your movement.",
                "ongoing_form_check": "Keep it up! Maintain steady pacing and concentrate on muscle tension."
            }
            
            if issue:
                # Targeted form corrections based on specific posture anomalies
                issue_lower = issue.lower()
                if "depth" in issue_lower or "squat" in issue_lower:
                    return "Squat a bit deeper to hit perfect parallel range of motion."
                elif "sagging" in issue_lower or "pike" in issue_lower:
                    return "Core tight! Keep your body fully straight and level during the push-up."
                elif "swing" in issue_lower:
                    return "Torso locked! Keep your body completely still and isolate the curl."
                elif "elbow" in issue_lower or "drift" in issue_lower:
                    return "Lock your elbows close to your ribs and keep them stable."
                elif "arch" in issue_lower:
                    return "Keep your spine neutral! Brace your abs to protect your lower back."
                elif "balance" in issue_lower:
                    return "Stay centered! Feet hip-width apart to maximize balance."
                return f"Focus on form: {issue}"
            
            return fallback_responses.get(event, "Great pacing! Stay focused and make every repetition count.")
    