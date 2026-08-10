# Polymorphism

class DataAnalyst:

    def work(self):
        print("Data Analyst analyzes data.")


class DataScientist:

    def work(self):
        print("Data Scientist builds predictive models.")


roles = [DataAnalyst(), DataScientist()]

for role in roles:
    role.work()
