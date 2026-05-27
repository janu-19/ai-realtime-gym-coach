from abc import ABC, abstractmethod
import math
class BaseExercise(ABC):
    def __init__(self):
        self.reps = 0
        self.stage=None
    def calculate_angle(self, a, b, c):
        ax,ay =a[0]-b[0], a[1]-b[1]
        cx,cy =c[0]-b[0], c[1]-b[1]
        dot = ax*cx + ay*cy
        mag_a=math.sqrt(ax**2 + ay**2)
        mag_c=math.sqrt(cx**2 + cy**2)
        if mag_a == 0 or mag_c == 0:
            return 0
        cos_angle = dot / (mag_a * mag_c)
        angle = math.acos(max(-1, min(1, cos_angle)))
        return math.degrees(angle)
    def get_points(self,landmarks,idx):
        p=landmarks[idx]
        return (p.x, p.y)
    def get_point(self, landmarks, idx):
        return self.get_points(landmarks, idx)
    @abstractmethod
    def process(self, landmarks):
        pass
    @abstractmethod
    def reset(self):
        pass   