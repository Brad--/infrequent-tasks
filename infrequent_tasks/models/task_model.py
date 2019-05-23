from datetime import date, timedelta
from dateutil.parser import parse


SEPARATOR = '\t'
SERIAL_NONE = 'None'


class TaskModel():
    # Populate TaskModel fields from a line in the user_tasks file
    #Pattern: name  repeat_frequency    complete    last_completion_date
    def deserialize(self, line):
        tokens = line.split(SEPARATOR)
        self.name = tokens[0]
        self.repeat_frequency = tokens[1]
        self.complete = eval(tokens[2])
        self.last_completion_date = self.getDateTimeFromISO8601String(tokens[3])

        if self.getResetDate() < date.today():
            self.setTodo()
    

    def getDateTimeFromISO8601String(self, s):
        if s.strip() == SERIAL_NONE:
            return None
        return parse(s).date()


    # Get string in serialized format for file write
    def getSerializedString(self):
        return SEPARATOR.join([self.name, self.repeat_frequency, str(self.complete), self.getSerializedLastCompletionDate()])


    def getSerializedLastCompletionDate(self):
        if self.last_completion_date == None:
            return SERIAL_NONE
        else:
            return self.last_completion_date.isoformat()


    def getResetDate(self):
        if not self.complete:
            return 0
        today = date.today()
        time_since_completion = abs(today - self.last_completion_date)

        repeat_unit = self.repeat_frequency[len(self.repeat_frequency) - 1:]
        repeat_num = int(self.repeat_frequency[:len(self.repeat_frequency) - 1])

        if repeat_unit == 'd':
            pass
        elif repeat_unit == 'm':
            repeat_num *= 30
        elif repeat_unit == 'y':
            repeat_num * 365 
        else:
            raise RuntimeError('Invalid unit specified for task "' + self.name + '"')

        reset_date = self.last_completion_date + timedelta(days = (repeat_num - time_since_completion.days))
        return reset_date


    def setTodo(self):
        self.complete = False
        self.last_completion_date = None


    def setDone(self):
        self.complete = True
        self.last_completion_date = date.today()


    def print(self):
        print(date.today().isoformat())
        print(self.getSerializedString())