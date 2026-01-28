from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Expense:
    amount: float 
    category : str
    description : str
    date : str = field(default_factory=lambda : datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive.")
