# आई Class = BCS_Aditi
class BCS_Aditi:
    def __init__(self):
        self.degree = "BCS"
        self.skill = "Python Basic"
    
    def code(self):
        print("मी BCS करून Code करते!")

# मुलगी Class = MCA_Aditi 
# ती BCS_Aditi कडून सगळं "Inherit" करते!
class MCA_Aditi(BCS_Aditi):
    def __init__(self):
        super().__init__()  # आईचं सगळं घे!
        self.degree = "BCS + MCA"  # आणि वरून Add कर!
        self.skill = "Python + Google Level"
    
    def google_job(self):  # नवीन Power!
        print("मी Google ला ₹50 Lakh ला जाणार!")

# बघ magic!
aditi = MCA_Aditi()
aditi.code()        # आईकडून मिळालं! "मी BCS करून Code करते!"
aditi.google_job()  # स्वतःचं! "मी Google ला ₹50 Lakh ला जाणार!"
print(aditi.degree) # BCS + MCA