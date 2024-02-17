class NumberStat:
     def __init__(self, _number = 0, _draw_count = 0, _ratio = 0) -> None:
          self.number = _number
          self.draw_count = _draw_count
          self.ratio = _ratio
          
     def to_str(self):
          return f"Number: {self.number}, Draw Count: {self.draw_count}, Ratio: {self.ratio}"     